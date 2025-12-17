import cohere
from src.core.config import settings

class CohereService:
    def __init__(self):
        self.client = cohere.Client(settings.COHERE_API_KEY)

    def embed_query(self, query: str) -> list[float]:
        response = self.client.embed(
            texts=[query],
            model="embed-english-v3.0",
            input_type="search_query"
        )
        return response.embeddings[0]

    def generate_response(self, prompt: str) -> str:
        response = self.client.chat(
            message=prompt,
            model="command-r-plus"
        )
        return response.text
