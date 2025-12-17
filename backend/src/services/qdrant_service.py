from qdrant_client import QdrantClient
from src.core.config import settings

class QdrantService:
    def __init__(self):
        self.client = QdrantClient(
            url=settings.QDRANT_URL, 
            api_key=settings.QDRANT_API_KEY
        )

    def create_collection_if_not_exists(self, collection_name: str, vector_size: int):
        self.client.recreate_collection(
            collection_name=collection_name,
            vectors_config={"size": vector_size, "distance": "Cosine"}
        )

    def search(self, collection_name: str, vector: list[float], limit: int) -> list:
        search_result = self.client.search(
            collection_name=collection_name,
            query_vector=vector,
            limit=limit
        )
        return search_result
