import requests
import trafilatura
from xml.etree import ElementTree

def fetch_sitemap_urls(sitemap_url: str) -> list[str]:
    response = requests.get(sitemap_url)
    root = ElementTree.fromstring(response.content)
    urls = [elem.text for elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    return urls

def extract_content_from_url(url: str) -> str:
    downloaded = trafilatura.fetch_url(url)
    return trafilatura.extract(downloaded)

import argparse
from src.services.cohere_service import CohereService
from src.services.qdrant_service import QdrantService
from qdrant_client.http.models import PointStruct

def ingest(sitemap_url: str, collection_name: str):
    cohere_service = CohereService()
    qdrant_service = QdrantService()

    qdrant_service.create_collection_if_not_exists(collection_name, vector_size=1024)

    urls = fetch_sitemap_urls(sitemap_url)
    for url in urls:
        print(f"Processing {url}")
        content = extract_content_from_url(url)
        if content:
            chunks = chunk_text(content)
            print(f"  Split into {len(chunks)} chunks.")
            
            embeddings = cohere_service.client.embed(
                texts=chunks,
                model="embed-english-v3.0",
                input_type="search_document"
            ).embeddings

            qdrant_service.client.upsert(
                collection_name=collection_name,
                points=[
                    PointStruct(
                        id=f"{url}#{i}",
                        vector=embedding,
                        payload={"text": chunk, "url": url, "chunk_id": i}
                    )
                    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings))
                ]
            )
            print(f"  Upserted {len(chunks)} chunks to Qdrant.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest book content into Qdrant.")
    parser.add_argument("--sitemap-url", type=str, default="https://q4-hackathon-ayio.vercel.app/sitemap.xml", help="The URL of the sitemap to crawl.")
    parser.add_argument("--collection-name", type=str, default="physical_ai_book", help="The name of the Qdrant collection.")
    args = parser.parse_args()

    ingest(args.sitemap_url, args.collection_name)
