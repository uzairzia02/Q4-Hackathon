from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.services.cohere_service import CohereService
from src.services.qdrant_service import QdrantService
from src.models.chat_session import ChatSession
import json

router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    selected_text: str | None = None
    user_id: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[dict]

@router.post("/chat", response_model=ChatResponse)

def chat(request: ChatRequest, db: Session = Depends(get_db)):

    cohere_service = CohereService()

    qdrant_service = QdrantService()



    # Combine query and selected text

    contextual_query = request.query

    if request.selected_text:

        contextual_query = f"{request.selected_text}\n\n{request.query}"



    # Embed the query

    query_embedding = cohere_service.embed_query(contextual_query)



    # Search for relevant chunks

    search_results = qdrant_service.search("physical_ai_book", query_embedding, limit=5)



    # Build the prompt

    context = "\n".join([result.payload["text"] for result in search_results])

    prompt = f"Based on the following context, answer the user's question.\n\nContext:\n{context}\n\nQuestion: {request.query}"



    # Generate the response

    answer = cohere_service.generate_response(prompt)

    sources = [{"url": result.payload["url"], "text": result.payload["text"]} for result in search_results]



    # Save the conversation

    chat_session = db.query(ChatSession).filter(ChatSession.user_id == request.user_id).first()

    if not chat_session:

        chat_session = ChatSession(user_id=request.user_id, conversation_history=[])

    

    chat_session.conversation_history.append({"question": request.query, "answer": answer})

    db.add(chat_session)

    db.commit()



    return {"answer": answer, "sources": sources}
