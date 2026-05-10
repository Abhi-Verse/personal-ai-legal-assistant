# AI Legal Assistant With CREWAI
# Project Overview

AI Legal Assistant With CREWAI is an intelligent multi-agent system designed to help users understand legal problems in simple language. The system identifies applicable IPC sections, retrieves relevant legal precedents, and generates AI-based legal drafts.

---

# Features

- IPC section identification using semantic search
- Retrieval-Augmented Generation (RAG)
- Multi-agent AI workflow using CrewAI
- Legal precedent retrieval from Indian Kanoon
- AI-generated FIR / legal draft generation
- Streamlit-based interactive web interface
- Voice input support
- Explainable AI future enhancement support

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CrewAI | Multi-agent orchestration |
| Streamlit | User interface |
| ChromaDB | Vector database |
| LangChain | RAG integration |
| HuggingFace Embeddings | Semantic embeddings |
| Groq API | Large language model |
| Tavily API | Legal web search |

---

# System Workflow

```text
User Input → AI Agents → IPC Retrieval → Precedent Search → Legal Draft Generation
```

---

# Main Modules

| Module | Function |
|---|---|
| Case Intake Module | Understands user legal issue |
| IPC Retrieval Module | Finds relevant IPC sections |
| Precedent Module | Searches related case laws |
| Drafting Module | Generates legal document |
| Voice Module | Supports speech input |

---

# Project Structure

```text
agents/             → AI agents
tasks/              → Task definitions
tools/              → Utility tools
voice/              → Voice interaction modules
chroma_vectordb/    → Vector database
app.py              → Main Streamlit application
```

---

# Installation Steps

## Step 1
Install Python 3.10 or above.

## Step 2
Install dependencies:

```bash
pip install -r requirements.txt
```

## Step 3
Create `.env` file and add API keys:

```env
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```

## Step 4
Build vector database:

```bash
python ipc_vectordb_builder.py
```

## Step 5
Run the application:

```bash
streamlit run app.py
```

---

# Future Enhancements

- Migration from IPC to BNS
- Hindi and regional language support
- Explainable AI integration
- Mobile application support
- Advanced voice assistant

---

# Limitations

- Supports criminal law only
- English-only support currently
- Requires internet connection
- Uses IPC framework currently

---
# Academic Purpose Notice

This project is developed for academic and educational purposes only. The generated legal information should not be considered professional legal advice.
