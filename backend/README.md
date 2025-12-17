# Integrated RAG Chatbot

This project is a Retrieval-Augmented Generation (RAG) chatbot that answers questions based on the content of the Physical AI book.

## Architecture

- **Backend**: FastAPI
- **LLM**: Cohere
- **Vector Store**: Qdrant
- **Database**: Neon Serverless Postgres

## Setup

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

## Data Ingestion

Run the ingestion script to process the book content and upload it to the Qdrant vector store:
```bash
python src/scripts/ingest.py
```

## Running the Backend

Start the FastAPI application:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Deployment

This application is designed to be deployed to Vercel as a serverless function.
