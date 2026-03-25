# 🤖 Personal AI RAG Assistant  
### *A Production-Ready Retrieval-Augmented Generation (RAG) Pipeline*

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://mini-rag-project-pq8w.onrender.com)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://mini-rag-project-mohit.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)

---

## 🚀 Live Demo

<p align="center">
  <a href="https://mini-rag-project-mohit.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀%20Launch%20App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  </a>
  <a href="https://mini-rag-project-pq8w.onrender.com/">
    <img src="https://img.shields.io/badge/⚙️%20Backend%20API-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  </a>
</p>

---

## 📸 Screenshots

### 🖥️ User Interface
<p align="center">
  <img src="./assets/ui.png" width="800"/>
</p>

### 💬 Query Examples

<p align="center">
  <img src="./assets/query.png" width="800"/>
  <br><br>
  <img src="./assets/query1.png" width="800"/>
  <br><br>
  <img src="./assets/query2.png" width="800"/>
</p>

---

## 🧠 Overview

This project presents a production-ready **Retrieval-Augmented Generation (RAG)** pipeline built for an AI chatbot as part of the Indecimal hiring process.

> 📝 Developed as part of a real-world hiring assignment, focusing on production constraints, scalability, and reliable LLM behavior.


💡 It enables users to:
- Query internal PDF documents (policies, specifications, FAQs)
- Receive **accurate, context-aware responses**
- Avoid **LLM hallucinations** using strict grounding techniques

---

## 🛠️ Tech Stack

| Component | Technology | Why? |
| :--- | :--- | :--- |
| **LLM** | `Nemotron-3-Nano-30B-A3B` | Strong reasoning with efficient inference via OpenRouter |
| **Embeddings** | `all-MiniLM-L6-v2` | Industry-standard semantic similarity model |
| **Vector Store** | `FAISS` | Fast similarity search for high-dimensional embeddings |
| **Backend** | `FastAPI` | High-performance async API framework |
| **Frontend** | `Streamlit` | Simple, interactive UI for rapid prototyping |
| **Infrastructure**| `Render` & `Streamlit Cloud` | Lightweight and scalable deployment |

---

## 🏗️ Architecture & Workflow

```
User Query → Streamlit UI
           → FastAPI Backend
           → Embedding Model (HF API)
           → FAISS Vector Store
           → Top-K Retrieval (k=3)
           → LLM (OpenRouter)
           → Grounded Response → UI
```

```mermaid
graph LR
    A[User Query] --> B[Streamlit UI]
    B --> C[FastAPI Backend]
    C --> D[Embedding Model - HF API]
    D --> E[FAISS Vector Store]
    E --> F[Top-K Retrieval - k=3]
    F --> G[LLM - OpenRouter]
    G --> H[Grounded Response]
    H --> B
```
---

## ⚙️ Implementation Details

### 1. Document Processing & Chunking
- Parsed PDFs using `PyPDF2`
- Split using `RecursiveCharacterTextSplitter`
- Used overlapping chunks to preserve semantic continuity

### 2. Vector Indexing & Retrieval
- Embeddings generated via Hugging Face Inference API
- Stored in local **FAISS index**
- Retrieved **Top-3 relevant chunks (k=3)** for each query

### 3. Grounded Answer Generation
- Strong **system prompt enforcement**
- Explicit fallback:  
  `"Answer not found in provided documents"`
- Low temperature (`0.2`) for factual consistency

---

## 🛡️ Production Optimizations

- ⚡ **Memory Optimization:** Switched to API-based embeddings to fit within Render's 512MB RAM limit  
- 🚀 **Lazy Loading:** Reduced startup time and ensured successful health checks  
- 🧩 **Decoupled Architecture:** Independent frontend & backend for scalability  
- 🔄 **Cold Start Handling:** Frontend polling mechanism for Render free-tier wake-up delays  

---

## 📊 Evaluation & Testing

The system was validated with real queries:

- ✅ Pricing-related queries (table lookup accuracy)  
- ✅ Specification-based queries (semantic retrieval)  
- ✅ Feature validation queries (factual correctness)  
- ❌ Out-of-context queries → Correctly rejected (anti-hallucination)

---

## 📦 Local Setup Instructions

> ⚠️ **Prerequisite:** Python **3.10 – 3.12** (tested on 3.12.2)

### 1. Clone the Repository
```bash
git clone https://github.com/Mohit9-y/mini-rag-project.git
cd mini-rag-project
```

### 2. Setup Backend
```bash
cd backend
pip install -r requirements.txt

# Create a .env file:
# OPENROUTER_API_KEY=your_key
# HF_TOKEN=your_huggingface_token

uvicorn main:app --reload
```

### 3. Setup Frontend
```bash
cd ../frontend
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔮 Future Improvements

- 🔐 Authentication & user sessions  
- 📂 Multi-document upload support  
- 🌐 Deployment with Docker & CI/CD  
- 📈 Monitoring & logging (Prometheus/Grafana)  

---

## 👨‍💻 Author

**Mohit Yadav**  

🎓 Final Year, B.Tech in Electronics & Instrumentation Engineering  
🏫 National Institute of Technology (NIT), Silchar  

📧 Email: mohitpsf@gmail.com  
🔗 LinkedIn: [Profile](https://www.linkedin.com/in/mohit-yadav-2a7a87388/)
💻 GitHub: [Mohit9-y](https://github.com/Mohit9-y)

---