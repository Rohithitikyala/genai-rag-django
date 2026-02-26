# GenAI RAG Assistant (Django + OpenAI)

## 📌 Project Overview
This project is a Retrieval-Augmented Generation (RAG) based GenAI Assistant built using Django and OpenAI APIs.  
It retrieves relevant information from a local knowledge base and generates context-aware responses.

---

# 🏗 Architecture Diagram

User → Frontend (HTML/JS) → Django Backend → RAG Engine → OpenAI API  
                                      ↓  
                                 Vector Store  
                                      ↓  
                                  data.json  

---

# 🔄 RAG Workflow Explanation

1. User sends a query from the frontend.
2. Django backend receives the query.
3. Query is converted into an embedding.
4. Similarity search is performed on stored document embeddings.
5. Top relevant chunks are selected.
6. Context + User Query is sent to LLM.
7. Generated answer is returned to frontend.

---

# 🧠 Embedding Strategy

- Model Used: text-embedding-3-small
- Each document is split into chunks (300 words).
- Each chunk is converted into a vector embedding.
- Stored in an in-memory vector store using NumPy.

Reason:
Chunking improves semantic search accuracy and reduces token usage.

---

# 🔎 Similarity Search Explanation

We use cosine similarity:

similarity = dot(A, B) / (||A|| × ||B||)

- Top 3 highest similarity chunks selected.
- Threshold: 0.75
- Only relevant content is passed to LLM.

This ensures:
- Reduced hallucination
- Context-based responses
- Efficient retrieval

---

# ✍ Prompt Design Reasoning

Prompt Structure:

"You are a helpful assistant. Answer the question using only the provided context."

Context:
{retrieved_chunks}

Question:
{user_query}

Reasoning:
- Restricts hallucination
- Forces grounded answers
- Improves accuracy

---

# ⚙ Setup Instructions

## 1️⃣ Clone Repository

git clone https://github.com/yourusername/genai-rag-django.git
cd genai-rag-django

## 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate   (Windows)

## 3️⃣ Install Dependencies

pip install -r requirements.txt

## 4️⃣ Add Environment Variables

Create `.env` file:

OPENAI_API_KEY=your_api_key_here

## 5️⃣ Run Server

python manage.py runserver

Open:
http://127.0.0.1:8000/

---

# 📸 Screenshots

(Add UI screenshots here)

---

# 🎥 Demo Video

(Add Google Drive / YouTube link here)

---

# 🚀 Technologies Used

- Django
- OpenAI API
- NumPy
- JavaScript
- HTML/CSS
