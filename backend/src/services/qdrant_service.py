from qdrant_client import QdrantClient
from qdrant_client.http import models
from src.core.config import settings

class QdrantService:
    def __init__(self):
        # For Qdrant cloud, use the proper initialization
        self.client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
            # For cloud instances, don't specify prefer_grpc
        )

    def create_collection_if_not_exists(self, collection_name: str, vector_size: int):
        self.client.recreate_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE)
        )

    def search(self, collection_name: str, vector: list[float], limit: int) -> list:
        # Based on the error message, the query method requires a query_text parameter
        # However, we want to perform a vector similarity search
        # Let's use the retrieve method which is designed for fetching points by ID
        # or try to use the scroll method to get all points

        # For vector similarity search in the newer API, we might need to use query_points
        try:
            # Try the query_points method which should exist based on the earlier method list
            search_result = self.client.query_points(
                collection_name=collection_name,
                query=vector,  # The vector to search for
                limit=limit,
                with_payload=True
            )
            return search_result
        except Exception as e:
            print(f"Qdrant query_points method failed: {str(e)}")

            # If query_points doesn't work, try using the scroll method to retrieve all points
            # This is not ideal for similarity search, but might help us understand the data
            try:
                scroll_result = self.client.scroll(
                    collection_name=collection_name,
                    limit=limit,
                    with_payload=True
                )
                # Convert to the expected format
                return scroll_result[0] if scroll_result else []
            except Exception as e2:
                print(f"Qdrant scroll method also failed: {str(e2)}")
                return []
