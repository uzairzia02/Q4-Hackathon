# Research: Integrated RAG Chatbot

**Date**: 2025-12-16
**Feature**: [specs/001-rag-chatbot/spec.md](specs/001-rag-chatbot/spec.md)

## 1. Web Scraping with `trafilatura`

- **Decision**: Use `trafilatura` in conjunction with `requests` to fetch and extract the main content from the book's sitemap URLs.
- **Rationale**: `trafilatura` is highly effective at removing boilerplate and extracting clean, relevant text, which is ideal for creating a high-quality corpus for the RAG system. It also supports sitemaps directly, simplifying the crawling process.
- **Best Practices to Apply**:
  - Use the sitemap URL (`https://q4-hackathon-ayio.vercel.app/sitemap.xml`) as the input for crawling.
  - Set a polite delay between requests to avoid overloading the server.
  - Extract only the main content to avoid including headers, footers, and navigation in the embeddings.

## 2. Content Chunking Strategy

- **Decision**: Implement a sentence-aware chunking strategy with a target size of 1000-1200 characters and an overlap of 100-200 characters.
- **Rationale**: This approach balances the need for semantically coherent chunks (by respecting sentence boundaries) with the context window limitations of the Cohere embedding model (`embed-english-v3.0`). The overlap ensures that sentences are not split across chunks, preserving context for better retrieval.
- **Alternatives Considered**: Fixed-size chunking (can split sentences), recursive chunking (more complex than necessary for this use case).

## 3. Qdrant Hybrid Search

- **Decision**: Use Qdrant's built-in hybrid search capabilities by creating a collection with both dense and sparse vectors. However, for the initial implementation, we will focus on dense vector search, as it is simpler and sufficient for a PoC.
- **Rationale**: While hybrid search (semantic + keyword) offers superior performance, it adds complexity. Starting with dense vector search allows for a faster initial implementation, and hybrid search can be added as a future enhancement if needed. Qdrant's architecture supports this phased approach.
- **Best Practices to Apply**:
  - Create a Qdrant collection with a vector size of 1024 to match Cohere's `embed-english-v3.0`.
  - Use COSINE distance for similarity search, as it is well-suited for normalized embeddings.
  - Store the original text, URL, and a unique chunk ID in the payload of each vector for easy retrieval and source citation.

## 4. FastAPI with Neon Serverless Postgres

- **Decision**: Use FastAPI with `psycopg2-binary` and SQLAlchemy for database interaction.
- **Rationale**: This is a standard and well-supported stack. FastAPI's asynchronous capabilities work well with modern database drivers, and SQLAlchemy provides a robust ORM for defining the data model. Neon's serverless nature handles scaling automatically.
- **Best Practices to Apply**:
  - Manage the database connection URL and other secrets using environment variables (e.g., via a `.env` file and `pydantic-settings`).
  - Use a dependency injection system to manage database sessions in FastAPI.
  - Define the `ChatSession` table using a SQLAlchemy declarative model.

## 5. Deployment to Vercel

- **Decision**: Deploy the FastAPI application as a Vercel Serverless Function.
- **Rationale**: Vercel provides a seamless deployment experience with excellent integration for Python backends. Its serverless architecture is a perfect fit for the project's security and efficiency principles, handling scaling automatically and minimizing costs.
- **Best Practices to Apply**:
  - Structure the project with an `api` directory containing the main FastAPI application file (`index.py` or `main.py`).
  - Use a `vercel.json` file to configure the build and routing.
  - Ensure all dependencies are listed in `requirements.txt`.
  - Place environment variables in the Vercel project settings.
