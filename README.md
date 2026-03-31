

# 📘 EduBot RAG API – Project Documentation

## 👨‍💻 Developer

Poovarasan                                       
Manikandan                                            
Vainavin

Python Full Stack Developer | AI Integration

---

## 📌 Project Title

**EduBot – AI-Based RAG Chatbot API (Ollama + ChromaDB + Flask)**

---

## Objective

The objective of this project is to build an AI-powered backend system that can:

* Ingest and process educational content
* Store knowledge efficiently using vector database
* Retrieve relevant information based on user queries
* Generate intelligent answers using a Large Language Model (LLM)

This system is designed to support **student learning and institutional academic assistance**.

---

##  System Overview

EduBot uses a **Retrieval-Augmented Generation (RAG)** architecture:

1. Documents are ingested and converted into embeddings
2. Embeddings are stored in a vector database
3. User queries are converted into embeddings
4. Relevant data is retrieved from the database
5. LLM generates contextual answers

---

## Technology Stack

* **Backend Framework**: Flask
* **LLM Runtime**: Ollama (LLaMA 3)
* **Embedding Model**: nomic-embed-text
* **Vector Database**: ChromaDB
* **Programming Language**: Python

---

##  System Architecture

User → API (Flask) → RAG Engine → Embedding Model → Vector DB → LLM → Response

---

##  Key Functional Modules

### 1️⃣ Data Ingestion Module

* Reads text files
* Splits content into chunks
* Generates embeddings
* Stores data in ChromaDB

---

### 2️⃣ Embedding Module

* Uses Ollama embedding model
* Converts text into numerical vectors

---

### 3️⃣ Retrieval Module

* Searches similar content using vector similarity
* Fetches relevant chunks

---

### 4️⃣ LLM Response Module

* Uses LLaMA 3 model via Ollama
* Generates answers based on retrieved context

---

### 5️⃣ API Layer (Flask)

Provides endpoints:

* `/ingest` → Upload and process documents
* `/ask` → Query the system
* `/` → Health check

---

##  Project Structure

```
EduBot/
│
├── app.py                 # Flask API
├── db/                    # ChromaDB storage
├── requirements.txt
└── modules (logic inside app)
```

---

## 🚀 Setup Instructions

### 1. Install Dependencies

```
pip install flask chromadb requests
```

### 2. Start Ollama

```
ollama run llama3
```

### 3. Run Application

```
python app.py
```

---

## 📌 API Usage

### 🔹 Ingest Data

POST `/ingest`

```
{
  "path": "sample.txt"
}
```

### 🔹 Ask Question

POST `/ask`

```
{
  "question": "Explain Python"
}
```

---

##  Use Cases

### For Students

* Doubt clarification
* Concept learning
* Self-study assistant

### For Institutions

* AI-based learning assistant
* Academic support system
* Student interaction tracking (future scope)

---

## Current Limitations

* Database resets on restart
* No authentication mechanism
* Limited to text file ingestion
* No UI (API-based only)

---

##  Future Enhancements

* PDF & document ingestion
* Streamlit-based UI integration
* Chat history memory
* Authentication & user tracking
* Deployment (cloud/server)

---

## Project Status

* Core RAG pipeline: ✅ Completed
* API integration: ✅ Completed
* Local LLM integration: ✅ Completed
* Production readiness: 🔄 In Progress

---

##  Conclusion

EduBot is a functional AI-based RAG system that demonstrates:

* Real-world LLM integration
* Vector database usage
* Context-aware response generation

This project can be extended into a **full-scale institutional AI assistant**.

-------------------Thank You---------------------
