from fastapi import APIRouter, Depends
from pydantic import BaseModel
from backend.src.services.rag import RAGService # Assuming RAGService is in this path

router = APIRouter()

class ChatRequest(BaseModel):
    question: str
    context: str | None = None # Optional context if selecting text from the book

@router.post("/chat")
def chat_with_rag(request: ChatRequest):
    rag_service = RAGService() # Initialize RAGService for each request (can be optimized with dependency injection) 
    
    # If context is provided (e.g., user selected text), prioritize it
    if request.context:
        query_text = f"Context: {request.context}\nQuestion: {request.question}"
    else:
        query_text = request.question

    response = rag_service.query_chatbot(query_text)
    return {"answer": response}
