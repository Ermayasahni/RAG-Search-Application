# RAG-Search-Application

## 🚀 Project Overview
A minimal Generative AI project using FastAPI, Streamlit, LangChain, FAISS, and Groq LLM for similarity and multiquery retrieval with prompt engineering.
This is a **Generative AI Retrieval-Augmented Generation (RAG) project** built using **FastAPI**, **Streamlit**, **LangChain**, **FAISS**, and **Groq LLM**.  

It allows users to:

- Query a small knowledge base (documents)
- Retrieve relevant information via **similarity search** or **multiquery search**
- Demonstrate **prompt engineering** for structured AI responses

---
## 🧠 Features

- **Similarity Search** – retrieve top-k relevant documents
- **MultiQuery Retrieval** – query multiple topics at once with Groq LLM
- **Prompt Engineering** – guide LLM responses via structured queries
- **Streamlit UI** – simple web interface
- **FAISS Vector Store** – embeddings-based search
- **FastAPI** – backend API

## 🛠 Tech Stack

 -  Python
 -  FastAPI
 -  Streamlit
 -  LangChain
 -  FAISS
 -  HuggingFace Embeddings
 -  Groq LLM

## 📂 Project Structure
GenAI-RAG-App/
│

├── backend/

│ └── main.py # FastAPI backend with LangChain retrieval
│

├── frontend/

│ └── app.py # Streamlit frontend
│

├── requirements.txt # Python dependencies

└── .env # API keys (e.g., GROQ_API_KEY)

Create Virtual Environment

python -m venv env

Windows:

    env\Scripts\activate

Linux/Mac:

   source env/bin/activate

Install Dependencies

   pip install -r requirements.txt

Add .env File

   GROQ_API_KEY=your_groq_api_key_here
   ▶️ Run the Application
Start Backend
   uvicorn backend.main:app --reload

Backend runs at:

    http://127.0.0.1:8000
    Start Frontend
    streamlit run frontend/app.py
    
🔗 API Endpoints
    1. Similarity Search

    POST /similarity

   Request

      {
        "query": "Tell me about Python and biodiversity"
      }

  Response

    {
      "results": [
        "Python is a popular programming language known for its simple syntax and readability.",
        "Python supports object-oriented and functional programming paradigms.",
        "Biodiversity refers to the variety of life on Earth including plants, animals, and microorganisms."
      ]
    }
2. MultiQuery Search

    POST /multiquery

    Request
    
    {
      "query": "Tell me about Python and biodiversity"
    }

Response

      {
        "results": [
          "Python is widely used for data science, web development, and AI applications.",
          "Protecting biodiversity is essential for ecosystem balance."
        ]
      }
🔥 Prompt Engineering

    The project demonstrates prompt engineering for better AI responses:
    
    You are a helpful AI assistant.
    Answer the user's question clearly and concisely.
    
    User Question:
    {user_query}
    
    Response:
    
    Helps control the output style
    
    Improves accuracy and relevance
    
    Makes AI responses structured and readable

