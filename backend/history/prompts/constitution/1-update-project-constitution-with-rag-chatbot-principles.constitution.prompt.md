---
id: 1
title: Update Project Constitution with RAG Chatbot Principles
stage: constitution
date: 2025-12-16
surface: agent
model: Gemini
feature: none
branch: main
user: uzairzia
command: /sp.constitution
labels: ["constitution", "rag", "cohere"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

/sp.constitution 
Project: Integrated RAG Chatbot Development using SpecifyKit Plus and Gemini CLI
Core principles:

Specification-driven development: All features must start from clear, verifiable specifications using SpecifyKit Plus templates
AI-assisted coding: Leverage Gemini CLI for code generation, debugging, and automation while maintaining human oversight
Modularity and scalability: Design for multi-agent patterns adapted from SpecifyKit Plus, replacing OpenAI with Cohere API
User-centric functionality: Prioritize accurate responses based on book content, including handling user-selected text
Security and efficiency: Use serverless components (Neon Postgres, Qdrant Free Tier) for cost-effective, secure deployment
Key standards:
LLM integration: Exclusively use Cohere API for embeddings, generation, and any agent behaviors; no OpenAI dependencies
Backend: FastAPI for API endpoints, with proper error handling and authentication
Database: Neon Serverless Postgres for storing metadata, user sessions, or non-vector data
Vector store: Qdrant Cloud Free Tier for book content embeddings and retrieval
Retrieval: Implement hybrid search (semantic + keyword) for robust RAG
User selection handling: Support context-aware queries on user-highlighted text
Testing: 100% coverage for core paths; use Gemini CLI for automated test generation
Documentation: Inline specs in code; full README with deployment instructions
Version control: Git-based, with branches for features/specs
Constraints:
API keys: Use Cohere API key only; manage securely via environment variables
Free tiers: Stay within Qdrant Free Tier limits (e.g., 1GB storage, basic queries)
Build tools: Primary development via Gemini CLI commands; SpecifyKit Plus for project structure
Performance: Response time under 2 seconds for typical queries
Compatibility: Web-embedded (e.g., in Vercel-hosted book); support modern browsers
No external installs: Stick to pre-installed libs in Gemini CLI environment where possible
Success criteria:
Functional RAG: Accurately answers 95% of book-related questions in blind tests
User text handling: Correctly processes and responds to selected text queries
Embedding success: Chatbot deployed and interactive within the published book
Spec compliance: All code traceable to initial specifications
Error-free deployment: Zero critical bugs in production
Cost: Zero or minimal (under $5/month) using free tiers

## Response snapshot

I have updated the project constitution at `.specify/memory/constitution.md` to reflect the principles, standards, constraints, and success criteria for the "Integrated RAG Chatbot Development" project. The constitution is now at version 1.0.0.

## Outcome

- ✅ Impact: The project's guiding principles are now formally documented, providing a clear framework for development and decision-making.
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md
- 🔁 Next prompts: none
- 🧠 Reflection: The provided principles were detailed and specific, allowing for a comprehensive constitution document to be created.

## Evaluation notes (flywheel)

- Failure modes observed: The `create-phr.sh` script mentioned in the instructions was not found.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Ensure the PHR creation script is available and functional in the specified path.
