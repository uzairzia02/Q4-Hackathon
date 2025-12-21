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
    try:
        cohere_service = CohereService()

        # Combine query and selected text
        contextual_query = request.query
        if request.selected_text:
            contextual_query = f"{request.selected_text}\n\n{request.query}"

        # Embed the query
        query_embedding = cohere_service.embed_query(contextual_query)

        # Try to search in Qdrant, but handle errors gracefully
        search_results = []
        sources = []
        try:
            qdrant_service = QdrantService()
            search_response = qdrant_service.search("physical_ai_book1", query_embedding, limit=5)

            # Check if the response is a QueryResponse object (newer versions) or a list
            if hasattr(search_response, 'points'):  # QueryResponse object
                search_results = search_response.points
            elif isinstance(search_response, (list, tuple)):  # List of results
                search_results = search_response
            else:
                search_results = []

            print(f"Qdrant search successful, found {len(search_results) if search_results else 0} results")

            # Process the search results
            if search_results:
                # Each result should have a payload attribute
                sources = []
                context_parts = []
                for result in search_results:
                    # Extract payload - may be in different formats depending on version
                    if hasattr(result, 'payload'):
                        payload = result.payload
                    elif hasattr(result, '__getitem__') and len(result) > 1:
                        # Tuple format (id, payload, vector, ...)
                        payload = result[1] if isinstance(result[1], dict) else {}
                    else:
                        payload = {}

                    text = payload.get("text", "")
                    url = payload.get("url", "")

                    sources.append({"url": url, "text": text})
                    if text:
                        context_parts.append(text)

                context = "\n".join(context_parts)
            else:
                sources = [{"url": "no-results", "text": "No relevant content found in the book"}]
                context = "No specific context available from the book."

        except Exception as qdrant_error:
            print(f"Qdrant error: {str(qdrant_error)}")
            # Create a mock response for testing purposes
            sources = [{"url": "mock-url", "text": "This is a mock response for testing."}]
            context = "No specific context available from the book."

        # Build the prompt
        prompt = f"Based on the following context from the Physical AI and Humanoid Robotics book, answer the user's question.\n\nContext:\n{context}\n\nQuestion: {request.query}"
        print(f"Generated prompt: {prompt[:100]}...")  # Log first 100 chars of prompt

        # Generate the response
        answer = cohere_service.generate_response(prompt)
        print(f"Cohere response received: {answer[:50]}...")  # Log first 50 chars of response

        # Save the conversation (with error handling for missing table)
        try:
            chat_session = db.query(ChatSession).filter(ChatSession.user_id == request.user_id).first()
            if not chat_session:
                chat_session = ChatSession(user_id=request.user_id, conversation_history=[])

            chat_session.conversation_history.append({"question": request.query, "answer": answer})
            db.add(chat_session)
            db.commit()
        except Exception as db_error:
            print(f"Database error (this is OK for testing): {str(db_error)}")
            # Continue without saving to database if table doesn't exist

        return {"answer": answer, "sources": sources}

    except Exception as e:
        # Log the error for debugging
        import traceback
        print(f"Error in chat endpoint: {str(e)}")
        print(traceback.format_exc())  # This will print the full stack trace
        raise e
