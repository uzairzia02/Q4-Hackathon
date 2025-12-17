# Tasks: Integrated RAG Chatbot

**Input**: Design documents from `specs/001-rag-chatbot/`
**Prerequisites**: `plan.md`, `spec.md`, `data-model.md`, `contracts/openapi.yaml`

## Phase 1: Setup

- [X] T001 Create project directories: `src/api`, `src/services`, `src/core`, `src/scripts`, `src/models`, `tests/unit`, `tests/integration`.
- [X] T002 Create `requirements.txt` and add: `fastapi`, `uvicorn`, `cohere`, `qdrant-client`, `psycopg2-binary`, `python-dotenv`, `requests`, `trafilatura`, `pytest`.
- [X] T003 [P] Create `.env` file in the root and add placeholders for `COHERE_API_KEY`, `QDRANT_API_KEY`, `QDRANT_URL`, `DATABASE_URL`.

## Phase 2: Foundational

- [X] T004 In `src/core/config.py`, implement a Pydantic `Settings` class to load environment variables.
- [X] T005 [P] In `src/core/logging.py`, configure structured logging for the application.
- [X] T006 In `src/core/database.py`, implement SQLAlchemy setup: engine, `SessionLocal`, and a `get_db` dependency.
- [X] T007 In `src/models/chat_session.py`, define the `ChatSession` SQLAlchemy model with columns based on `data-model.md`.
- [X] T008 [P] In `src/services/cohere_service.py`, create a `CohereService` class with methods for `embed_query` and `generate_response`.
- [X] T009 [P] In `src/services/qdrant_service.py`, create a `QdrantService` class with methods for `create_collection_if_not_exists` and `search`.

## Phase 3: Data Ingestion Pipeline

**Goal**: Create a script to crawl, chunk, and embed the book content into the vector store.
**Independent Test**: The Qdrant collection `physical_ai_book` is populated with vector embeddings and payloads.

- [X] T010 In `src/scripts/ingest.py`, create a function to fetch URLs from the sitemap.
- [X] T011 [P] In `src/scripts/ingest.py`, create a function that takes a URL, uses `trafilatura` to extract content.
- [X] T012 In `src/scripts/ingest.py`, create a function for sentence-aware chunking of the extracted text.
- [X] T013 In `src/scripts/ingest.py`, create a main `ingest` function that orchestrates crawling, chunking, and calling the embedding service.
- [X] T014 Integrate `CohereService` in `src/scripts/ingest.py` to generate embeddings for each chunk.
- [X] T015 Integrate `QdrantService` in `src/scripts/ingest.py` to upsert the vectors and payloads into the collection.
- [X] T016 Add `argparse` to `src/scripts/ingest.py` to allow running from the command line.

## Phase 4: User Story 1 - Ask a question about the book

**Goal**: Implement the core functionality of the chatbot to answer questions based on the book's content.
**Independent Test**: The `/chat` endpoint can receive a query and return a relevant answer with sources.

- [X] T017 [US1] In `src/main.py`, create the main FastAPI app instance and include the chat API router.
- [X] T018 [US1] In `src/api/chat.py`, create an `APIRouter` and define the Pydantic models for the `/chat` request and response schemas from `openapi.yaml`.
- [X] T019 [US1] In `src/api/chat.py`, implement the `/chat` POST endpoint.
- [X] T020 [US1] In the `/chat` endpoint, call `CohereService` to embed the incoming query.
- [X] T021 [US1] In the `/chat` endpoint, call `QdrantService` to perform a semantic search with the query embedding.
- [X] T022 [US1] In the `/chat` endpoint, construct a detailed prompt for the generation model, including the retrieved context chunks.
- [X] T023 [US1] In the `/chat` endpoint, call `CohereService` to generate a response based on the prompt. (Covers FR-008 source citation).
- [X] T024 [US1] In the `/chat` endpoint, implement logic to save the Q&A to the `ChatSession` in the database.

## Phase 5: User Story 2 - Query on user-selected text

**Goal**: Enhance the chatbot to handle queries on user-selected text.
**Independent Test**: The `/chat` endpoint can process the `selected_text` parameter and return a context-aware answer.

- [X] T025 [US2] Modify the `/chat` Pydantic request model in `src/api/chat.py` to include the optional `selected_text` field.
- [X] T026 [US2] In the `/chat` endpoint logic, if `selected_text` is present, prepend it to the user's query to form a new contextual query before embedding.

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T027 [P] In `tests/unit/test_services.py`, write unit tests for `CohereService` and `QdrantService` using mocks.
- [X] T028 [P] In `tests/unit/test_ingest.py`, write unit tests for the chunking logic in the ingestion script.
- [X] T029 [P] In `tests/integration/test_chat_api.py`, write an integration test for the `/chat` endpoint, mocking external API calls.
- [X] T030 In `src/main.py`, add middleware for logging API requests and responses. (Covers OB-001).
- [X] T031 In `src/main.py`, add a generic exception handler to log errors and return a standard error response. (Covers OB-002).
- [X] T032 [P] Create a comprehensive `README.md` with sections for architecture, setup, environment variables, and deployment.

## Dependencies & Execution Order

- **Phase 1 & 2** must be complete before other phases.
- **Phase 3** (Data Ingestion) can run after Phase 2.
- **Phase 4** (US1) can start after Phase 2. It depends on Phase 3 for data.
- **Phase 5** (US2) depends on Phase 4.
- **Phase 6** (Polish) can be worked on incrementally after the relevant components are built.