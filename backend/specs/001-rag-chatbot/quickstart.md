# Quickstart: Integrated RAG Chatbot

**Date**: 2025-12-16
**Feature**: [specs/001-rag-chatbot/spec.md](specs/001-rag-chatbot/spec.md)

This document provides a quickstart guide for setting up and running the RAG chatbot backend.

## Prerequisites

- Python 3.11+
- Poetry (or pip) for dependency management
- Access to the Cohere API, Qdrant Cloud, and Neon Serverless Postgres

## 1. Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create a `.env` file** in the root of the project and add the following environment variables:
    ```
    COHERE_API_KEY="your-cohere-api-key"
    QDRANT_API_KEY="your-qdrant-api-key"
    QDRANT_URL="your-qdrant-url"
    DATABASE_URL="your-neon-database-url"
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 2. Data Ingestion

Run the ingestion script to process the book content and upload it to the Qdrant vector store:
```bash
python src/scripts/ingest.py
```

## 3. Running the Backend

Start the FastAPI application:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## 4. API Usage

You can interact with the API using the automatically generated Swagger documentation at `http://127.0.0.1:8000/docs`.

### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-d 
'{'
  "query": "What is Retrieval-Augmented Generation?",
  "selected_text": ""
}'
```

### Example Response

```json
{
  "answer": "Retrieval-Augmented Generation (RAG) is a technique that combines a retriever and a generator to answer questions.",
  "sources": [
    {
      "url": "https://example.com/page/1",
      "text": "..."
    }
  ]
}
```
