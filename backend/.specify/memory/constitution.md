<!--
Sync Impact Report:

- Version change: 0.0.0 → 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] → I. Specification-Driven Development
  - [PRINCIPLE_2_NAME] → II. AI-Assisted Coding
  - [PRINCIPLE_3_NAME] → III. Modularity and Scalability
  - [PRINCIPLE_4_NAME] → IV. User-Centric Functionality
  - [PRINCIPLE_5_NAME] → V. Security and Efficiency
- Added sections:
  - Key Standards
  - Constraints
  - Success Criteria
- Removed sections:
  - [SECTION_2_NAME]
  - [SECTION_3_NAME]
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Integrated RAG Chatbot Development using SpecifyKit Plus and Gemini CLI Constitution

## Core Principles

### I. Specification-Driven Development
All features must start from clear, verifiable specifications using SpecifyKit Plus templates. This ensures that development is aligned with requirements from the outset.

### II. AI-Assisted Coding
Leverage Gemini CLI for code generation, debugging, and automation while maintaining human oversight. This accelerates development and improves code quality.

### III. Modularity and Scalability
Design for multi-agent patterns adapted from SpecifyKit Plus, replacing OpenAI with Cohere API. This allows for flexible and scalable architecture.

### IV. User-Centric Functionality
Prioritize accurate responses based on book content, including handling user-selected text. The system must be intuitive and provide value to the end-user.

### V. Security and Efficiency
Use serverless components (Neon Postgres, Qdrant Free Tier) for cost-effective, secure deployment. Security and performance are non-negotiable aspects of the architecture.

## Key Standards

- **LLM Integration**: Exclusively use Cohere API for embeddings, generation, and any agent behaviors; no OpenAI dependencies.
- **Backend**: FastAPI for API endpoints, with proper error handling and authentication.
- **Database**: Neon Serverless Postgres for storing metadata, user sessions, or non-vector data.
- **Vector Store**: Qdrant Cloud Free Tier for book content embeddings and retrieval.
- **Retrieval**: Implement hybrid search (semantic + keyword) for robust RAG.
- **User Selection Handling**: Support context-aware queries on user-highlighted text.
- **Testing**: 100% coverage for core paths; use Gemini CLI for automated test generation.
- **Documentation**: Inline specs in code; full README with deployment instructions.
- **Version Control**: Git-based, with branches for features/specs.

## Constraints

- **API Keys**: Use Cohere API key only; manage securely via environment variables.
- **Free Tiers**: Stay within Qdrant Free Tier limits (e.g., 1GB storage, basic queries).
- **Build Tools**: Primary development via Gemini CLI commands; SpecifyKit Plus for project structure.
- **Performance**: Response time under 2 seconds for typical queries.
- **Compatibility**: Web-embedded (e.g., in Vercel-hosted book); support modern browsers.
- **No External Installs**: Stick to pre-installed libs in Gemini CLI environment where possible.

## Success Criteria

- **Functional RAG**: Accurately answers 95% of book-related questions in blind tests.
- **User Text Handling**: Correctly processes and responds to selected text queries.
- **Embedding Success**: Chatbot deployed and interactive within the published book.
- **Spec Compliance**: All code traceable to initial specifications.
- **Error-Free Deployment**: Zero critical bugs in production.
- **Cost**: Zero or minimal (under $5/month) using free tiers.

## Governance

Amendments to this constitution require documentation, a clear rationale, and an approved migration plan. All development activities, including code reviews and quality gates, must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-16 | **Last Amended**: 2025-12-16