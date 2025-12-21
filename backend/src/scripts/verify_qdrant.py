"""
Script to verify that the Qdrant collection contains your book data
"""
from src.services.qdrant_service import QdrantService
from src.services.cohere_service import CohereService

def verify_qdrant_data(collection_name: str = "physical_ai_book"):
    """
    Verify that the Qdrant collection exists and contains data
    """
    qdrant_service = QdrantService()

    # Check if collection exists
    try:
        collections = qdrant_service.client.get_collections()
        collection_names = [col.name for col in collections.collections]

        if collection_name in collection_names:
            print(f"[SUCCESS] Collection '{collection_name}' exists")

            # Get collection info
            collection_info = qdrant_service.client.get_collection(collection_name)
            print(f"[INFO] Points count: {collection_info.points_count}")

            if collection_info.points_count > 0:
                # Try to retrieve a few points to verify content
                limit = min(3, collection_info.points_count)
                records = qdrant_service.client.scroll(
                    collection_name=collection_name,
                    limit=limit,
                    with_payload=True,
                    with_vectors=False
                )

                print(f"\n[INFO] Sample records from '{collection_name}':")
                for i, (record, _) in enumerate(records):
                    payload = record.payload
                    print(f"\nRecord {i+1}:")
                    print(f"  ID: {record.id}")
                    print(f"  URL: {payload.get('url', 'N/A')}")
                    print(f"  Text snippet: {payload.get('text', '')[:100]}...")
            else:
                print(f"[ERROR] Collection '{collection_name}' exists but is empty")
        else:
            print(f"[ERROR] Collection '{collection_name}' does not exist")
            print(f"Available collections: {collection_names}")

    except Exception as e:
        print(f"[ERROR] Error accessing Qdrant: {str(e)}")
        import traceback
        traceback.print_exc()

def test_search(collection_name: str = "physical_ai_book"):
    """
    Test searching in the collection with a sample query
    """
    print(f"\n[INFO] Testing search functionality on '{collection_name}'...")

    qdrant_service = QdrantService()
    cohere_service = CohereService()

    # Create a sample query
    sample_query = "What is physical AI?"
    query_embedding = cohere_service.embed_query(sample_query)

    try:
        search_results = qdrant_service.search(collection_name, query_embedding, limit=3)

        if search_results:
            print(f"[SUCCESS] Found {len(search_results)} results for query: '{sample_query}'")
            for i, result in enumerate(search_results):
                print(f"\nResult {i+1}:")
                print(f"  Score: {result.score}")
                print(f"  URL: {result.payload.get('url', 'N/A')}")
                print(f"  Text snippet: {result.payload.get('text', '')[:150]}...")
        else:
            print(f"[ERROR] No results found for query: '{sample_query}'")
            print("This could mean:")
            print("  - The collection is empty")
            print("  - The collection doesn't exist")
            print("  - The embeddings don't match well with the query")

    except Exception as e:
        print(f"[ERROR] Error during search: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("[INFO] Verifying Qdrant collection...")
    verify_qdrant_data()
    test_search()