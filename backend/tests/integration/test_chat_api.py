from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_chat_endpoint():
    # This is a basic test that does not mock external services.
    # A full integration test would require mocking Cohere and Qdrant.
    response = client.post("/chat", json={"query": "What is RAG?", "user_id": "test_user"})
    assert response.status_code == 200
    assert "answer" in response.json()
    assert "sources" in response.json()
