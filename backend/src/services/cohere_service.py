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
        # According to recent Cohere updates, the newer models to try are:
        # Try the newer Cohere models (as of post-September 2025)
        models_to_try = ['command-r-08-2024', 'command-r-plus-08-2024', 'command-light']

        for model in models_to_try:
            try:
                response = self.client.chat(
                    message=prompt,
                    model=model
                )
                return response.text
            except Exception as e:
                print(f"Model {model} failed: {str(e)}")
                continue

        # If all models fail, return a default response
        return "I'm sorry, but I'm currently experiencing issues with the AI service. Please try again later."
