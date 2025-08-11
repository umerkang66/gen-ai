# Chat-PDF 📄💬

Chat-PDF is a full-stack web application that transforms your static PDF documents into interactive conversational partners. Upload a PDF and start asking questions, summarizing content, and finding information instantly.

This project is built with a modern tech stack, leveraging the power of Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) to provide a seamless and intuitive user experience.

## ✨ Features

- **Interactive Chat Interface:** Converse with your documents in a natural, real-time chat.
- **Secure User Authentication:** User accounts and secure sessions.
- **PDF Upload & Processing:** Asynchronous processing of uploaded PDFs using a background worker.
- **Conversation History:** Your conversations with each document are saved and can be revisited.
- **Streaming Responses:** Assistant responses are streamed in real-time for a better user experience.
- **Built on RAG:** Utilizes a robust Retrieval-Augmented Generation architecture for accurate, context-aware answers.

## 🏗️ Architecture Overview

The application uses a Retrieval-Augmented Generation (RAG) architecture. The flow is as follows:

```
1. User Uploads PDF
      │
      └───> Backend API (FastAPI)
                  │
                  └───> Background Worker (Celery)
                              │
                              ├───> 1. Chunks PDF text
                              ├───> 2. Creates embeddings (OpenAI)
                              └───> 3. Stores in Vector DB (Pinecone)

2. User Asks a Question
      │
      └───> Frontend (Svelte)
                  │
                  └───> Backend API (FastAPI)
                              │
                              ├───> 1. Creates embedding for question
                              ├───> 2. Queries Vector DB for relevant context
                              ├───> 3. Constructs prompt with context
                              ├───> 4. Gets streaming response from LLM (OpenAI)
                              │
                              └───> Streams response back to Frontend
```

## 🛠️ Tech Stack

**Backend:**

- **Framework:** FastAPI
- **Async Tasks:** Celery with Redis
- **Database:** SQLAlchemy (connects to PostgreSQL, SQLite, etc.)
- **AI/LLM Orchestration:** LangChain
- **LLM & Embeddings:** OpenAI
- **Vector Database:** Pinecone
- **Dependency Management:** Pipenv

**Frontend:**

- **Framework:** SvelteKit
- **Build Tool:** Vite
- **Styling:** Tailwind CSS
- **UI Components:** Preline UI

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

- Python 3.10+
- Pipenv: `pip install pipenv`
- Node.js and npm

### 1. Clone the Repository

```bash
git clone <repository-url>
cd chat-pdf
```

### 2. Backend Setup

The backend is managed with `pipenv`.

**a. Configure Environment Variables:**

Create a `.env` file in the root directory by copying the example file.

```bash
cp .env.example .env
```

Now, open the `.env` file and fill in the required API keys and configuration values:

```ini
OPENAI_API_KEY=sk-...
SECRET_KEY=a-very-secret-key
SQLALCHEMY_DATABASE_URI=sqlite:///sqlite.db  # Or your postgres URI
REDIS_URI=redis://localhost:6379/0
PINECONE_API_KEY=...
PINECONE_ENV_NAME=...
PINECONE_INDEX_NAME=...
# Optional for LangSmith tracing
LANGFUSE_PUBLIC_KEY=...
LANGFUSE_SECRET_KEY=...
```

**b. Install Dependencies:**

Use `pipenv` to install the required Python packages. This will create a virtual environment.

```bash
pipenv install
```

**c. Initialize the Database:**

Run the command to create the database tables.

```bash
pipenv run invoke create_db
```

**d. Run the Backend Servers:**

You need to run two processes: the web server and the celery worker.

- **Terminal 1: Start the FastAPI Web Server:**

  ```bash
  pipenv run invoke dev
  ```

  The API will be available at `http://127.0.0.1:8000`.

- **Terminal 2: Start the Celery Worker:**
  ```bash
  pipenv run invoke devworker
  ```
  The worker will automatically pick up PDF processing tasks.

### 3. Frontend Setup

The frontend is a SvelteKit application located in the `client` directory.

**a. Navigate to the Client Directory:**

```bash
cd client
```

**b. Install Dependencies:**

```bash
npm install
```

**c. Run the Frontend Development Server:**

```bash
npm run dev
```

The application will be available at `http://localhost:5173`.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
