# Data Model: Integrated RAG Chatbot

**Date**: 2025-12-16
**Feature**: [specs/001-rag-chatbot/spec.md](specs/001-rag-chatbot/spec.md)

This document outlines the data models for the entities defined in the feature specification.

## 1. Book Content Chunk

This entity represents a chunk of text from the book, stored in the Qdrant vector store.

- **`id`**: A unique identifier for the chunk (e.g., UUID).
- **`vector`**: The 1024-dimensional vector embedding of the chunk's content.
- **`payload`**:
  - **`text`**: The original text content of the chunk.
  - **`url`**: The source URL of the page containing the chunk.
  - **`chunk_id`**: A sequential identifier for the chunk within its page.

## 2. Chat Session

This entity represents a conversation with a user, stored in the Neon Serverless Postgres database.

- **`id`**: A unique identifier for the session (e.g., UUID).
- **`user_id`**: A unique identifier for the user.
- **`conversation_history`**: A JSON field storing a list of question-and-answer pairs.
- **`created_at`**: A timestamp indicating when the session was created.
- **`updated_at`**: A timestamp indicating when the session was last updated.
