from fastapi import FastAPI
from pydantic import BaseModel
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class QueryRequest(BaseModel):
    query: str


docs = [
    Document(
        page_content="Regular exercise such as walking, jogging, or yoga helps maintain good physical health.",
        metadata={"topic": "exercise"}
    ),
    Document(
        page_content="Eating a balanced diet with fruits, vegetables, proteins, and whole grains improves overall health.",
        metadata={"topic": "diet"}
    ),
    Document(
        page_content="Sleeping 7-8 hours daily helps the body recover and supports mental health.",
        metadata={"topic": "sleep"}
    ),
    Document(
        page_content="Python is a popular programming language known for its simple syntax and readability.",
        metadata={"topic": "python"}
    ),
    Document(
        page_content="Python supports object-oriented and functional programming paradigms.",
        metadata={"topic": "python"}
    ),
    Document(
        page_content="Biodiversity refers to the variety of life on Earth including plants, animals, and microorganisms.",
        metadata={"topic": "biodiversity"}
    ),
]

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.from_documents(docs, embedding_model)

similarity_retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
    llm=ChatGroq(model="llama-3.1-8b-instant")
)


@app.post("/similarity")
def similarity_search(request: QueryRequest):
    results = similarity_retriever.invoke(request.query)

    response = [doc.page_content for doc in results]

    return {"results": response}


@app.post("/multiquery")
def multiquery_search(request: QueryRequest):
    results = multiquery_retriever.invoke(request.query)

    response = [doc.page_content for doc in results]

    return {"results": response}