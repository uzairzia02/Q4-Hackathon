---
id: 3
title: Plan RAG Chatbot Implementation
stage: plan
date: 2025-12-16
surface: agent
model: Gemini
feature: 001-rag-chatbot
branch: 001-rag-chatbot
user: uzairzia
command: /sp.plan
labels: ["plan", "rag", "chatbot"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-rag-chatbot/plan.md
 - specs/001-rag-chatbot/research.md
 - specs/001-rag-chatbot/data-model.md
 - specs/001-rag-chatbot/contracts/openapi.yaml
 - specs/001-rag-chatbot/quickstart.md
tests:
 - none
---

## Prompt

/sp.plan Integrated RAG Chatbot Development – Execution Plan

Project Overview
Develop a Retrieval-Augmented Generation (RAG) chatbot backend for integration into the Vercel-hosted Physical AI book. The chatbot must answer questions based solely on the book’s content, support queries on user-selected/highlighted text via API parameters, and be built exclusively with Cohere API, FastAPI backend, Neon Serverless Postgres, and Qdrant Cloud Free Tier. Frontend integration and embedding will be handled separately later.

Milestones & Phases (1-2 week timeline)

Phase 1: Project Setup and Specification (Days 1-2)
- Use SpecifyKit Plus to generate detailed specifications for all features, based on constitution templates
- Initialize Git repository with branches for ingestion, backend, and testing
- Set up environment variables for API keys (Cohere, Qdrant, Neon Postgres)
- Leverage Gemini CLI for initial code scaffolding and debugging setup
Deliverable: Verified specifications document and project repo structure

Phase 2: Data Ingestion Pipeline (Days 3-5)
- Crawl book content via sitemap[](https://q4-hackathon-ayio.vercel.app/sitemap.xml) using requests and trafilatura for text extraction
- Implement safe chunking (sentence-aware, 1000-1200 chars with 100-200 char overlap)
- Generate embeddings using Cohere "embed-english-v3.0" (input_type="search_document")
- Connect to Qdrant Free Tier:
  - Cluster ID: 9cd1125c-a5ee-47ca-87f3-adaf2aca9c95
  - Endpoint: https://9cd1125c-a5ee-47ca-87f3-adaf2aca9c95.europe-west3-0.gcp.cloud.qdrant.io
  - API Key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.Q6Qu4oTDbAJ5L-AdhFW5y6nGesHmcOYRdLyBRR-YHY0
- Create collection "physical_ai_book" (or similar) with COSINE distance, size=1024
- Upsert chunks with payload including text, URL, chunk_id
- Add retries, error handling, and monitor storage to stay under 1GB free tier limit
- Use Gemini CLI to generate and test ingestion script
Deliverable: Populated Qdrant collection with 150-300 chunks covering the full book; ingestion script in repo

Phase 3: FastAPI Backend Development (Days 6-9)
- Scaffold FastAPI app using Gemini CLI for code generation
- Implement /chat endpoint:
  - Parameters: query (str), selected_text (optional str)
  - Embed query with Cohere
  - Perform hybrid retrieval in Qdrant: semantic search (top-k=5-8) + keyword filters if applicable
  - If selected_text provided, embed it and use as additional context or boost in retrieval
  - Generate response using Cohere "command-r-plus" (or equivalent): prompt to answer only from context, cite sources (URLs)
- Integrate Neon Serverless Postgres for session management:
  - URL: postgresql://neondb_owner:npg_ybdVP8Et7hBU@ep-mute-frog-adngvlal-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
  - Schema: tables for conversations (optional for v1, but include basic setup)
- Add proper error handling, logging, CORS for future frontend, and basic API key auth
- Optimize for <2s response time: caching embeds if possible within free tiers
- Use Gemini CLI for automated test generation (pytest): cover retrieval, generation, selected_text handling
Deliverable: Fully tested FastAPI backend with /chat endpoint; deployed to Vercel Serverless (API-ready for frontend)

Phase 4: Testing and Optimization (Days 10-12)
- Run blind tests: 20+ book questions, verify 95%+ accuracy with citations
- Test user-selected text: 10+ scenarios, ensure context prioritization
- Performance testing: simulate loads, confirm <2s responses
- Security audit: env var usage, no hard-coded keys
- Documentation: Inline specs in code, full README with architecture, env setup, deployment guide
- Use Gemini CLI for debugging and optimization
Deliverable: Test reports confirming success criteria; optimized, documented code

Phase 5: Deployment and Handoff (Days 13-14)
- Deploy FastAPI to Vercel (serverless functions)
- Verify integration with Qdrant and Neon on free tiers
- Monitor costs (<$5/month)
- Final spec compliance check: trace all code to SpecifyKit Plus specs
Deliverable: Live backend API; handoff docs for future frontend integration

Dependencies & Risks
- Cohere API key: OwR0MgBu6o47fBUXA1PX379Up0iONX2004n5EMzo – handle securely in env vars
- Rate limits (Cohere/Qdrant): implement exponential backoff
- Storage limits: compress chunks if needed
- Gemini CLI dependencies: stick to pre-installed libs

Out of Scope (as per specify and user note)
- Frontend widget/embedding (handled later)
- Custom LLM fine-tuning
- Paid service tiers
- Advanced auth
- Multi-language/non-English support
- Standalone apps

Final Success Validation
- Backend deploys error-free on free tiers
- Accurately handles book questions and selected text via API
- 100% test coverage for core paths
- All features traceable to specs
- Ready for frontend integration in the published book
- Zero/minimal cost operation

## Response snapshot

I have created a detailed implementation plan for the RAG chatbot feature. The plan is located at `specs/001-rag-chatbot/plan.md`. I have also created the following design artifacts:
- `specs/001-rag-chatbot/research.md`
- `specs/001-rag-chatbot/data-model.md`
- `specs/001-rag-chatbot/contracts/openapi.yaml`
- `specs/001-rag-chatbot/quickstart.md`

## Outcome

- ✅ Impact: A comprehensive plan is now in place for the implementation of the RAG chatbot feature.
- 🧪 Tests: none
- 📁 Files: 
  - specs/001-rag-chatbot/plan.md
  - specs/001-rag-chatbot/research.md
  - specs/001-rag-chatbot/data-model.md
  - specs/001-rag-chatbot/contracts/openapi.yaml
  - specs/001-rag-chatbot/quickstart.md
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: The planning phase was successful, but the failure of the `update-agent-context.ps1` script indicates a need to be more robust to script failures.

## Evaluation notes (flywheel)

- Failure modes observed: The `update-agent-context.ps1` script failed to correctly parse the `plan.md` file.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Manually verify the functionality of the scripts in the `.specify/scripts` directory.
