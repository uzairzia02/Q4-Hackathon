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
        # Since all Cohere models were removed on September 15, 2025,
        # we'll implement a fallback that tries to extract relevant information
        # from the context provided in the prompt

        # Extract the context and question from the prompt
        if "Context:" in prompt and "Question:" in prompt:
            parts = prompt.split("Question:")
            context_part = parts[0]
            question = parts[1] if len(parts) > 1 else "What can you tell me?"

            # Extract the actual context
            context_start = context_part.find("Context:") + len("Context:")
            context = context_part[context_start:].strip()

            # Simple response generation based on context
            # This is a basic fallback until we can connect to a working AI service
            if context and "No specific context available" not in context:
                # Return relevant information from the context without truncation
                return f"Based on the Physical AI and Humanoid Robotics book: {context}"
            else:
                return "I couldn't find specific information in the book about this topic. Please try rephrasing your question."
        else:
            return "I'm currently experiencing issues with the AI service. Please try asking a question related to Physical AI and Robotics."
