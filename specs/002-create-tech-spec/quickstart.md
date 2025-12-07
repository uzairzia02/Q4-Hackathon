# Quickstart Guide: Physical AI Book Development Environment

This guide provides instructions to quickly set up your local development environment for the Physical AI Book project.

## 1. Prerequisites

Before you begin, ensure you have the following installed:

- **Git**: For version control.
- **Node.js** (LTS version): For Docusaurus development.
- **Python 3.11+**: For the FastAPI backend and Gemini CLI.
- **Poetry**: Python dependency management (recommended).
- **Docker / Docker Desktop**: For Qdrant and Neon Postgres (local development).
- **Gemini API Key**: For interacting with Gemini models.

## 2. Clone the Repository

```bash
git clone https://github.com/uzairzia02/Q4-Hackathon.git
cd Q4-Hackathon
```

## 3. Frontend Setup (Docusaurus)

Navigate to the `frontend/` directory and install dependencies:

```bash
cd frontend
npm install
# Or: yarn install
```

To start the Docusaurus development server:

```bash
npm start
# Or: yarn start
```

This will open the book in your browser at `http://localhost:3000`.

## 4. Backend Setup (FastAPI, Qdrant, Neon Postgres)

### 4.1 Environment Variables

Create a `.env` file in the `backend/` directory with the following variables:

```ini
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
QDRANT_HOST="localhost"
QDRANT_PORT="6333"
NEON_DATABASE_URL="postgresql://user:password@localhost:5432/mydatabase"
```

Replace placeholders with your actual credentials or local Docker service addresses.

### 4.2 Python Dependencies

Navigate to the `backend/` directory and install Python dependencies using Poetry:

```bash
cd backend
poetry install
poetry shell
```

### 4.3 Database and Vector Store (Docker)

Use Docker Compose to spin up local instances of Qdrant and Neon Postgres:

```bash
cd .. # Go back to project root if you are in backend/
docker-compose up -d qdrant neon-postgres
```

This will start Qdrant on port 6333 and Neon Postgres on port 5432.

### 4.4 Run Backend

```bash
cd backend
poetry run uvicorn main:app --reload
```

The FastAPI backend will be available at `http://localhost:8000`.

## 5. Gemini CLI Setup

Ensure the Gemini CLI is configured with your project. If you are using this CLI as the development environment, it should already be set up.

## Next Steps

- Explore the Docusaurus content in your browser.
- Experiment with the FastAPI backend endpoints using a tool like Postman or Insomnia.
- Begin integrating the RAG chatbot functionality.
