
from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[1]

# Chroma database path
DB_PATH = BASE_DIR / "vector_db"


# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Load existing vector database
vectorstore = Chroma(
    persist_directory=str(DB_PATH),
    collection_name="devdocs",
    embedding_function=embeddings
)


# Create MMR retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 3,
        "fetch_k": 10
    }
)


def retrieve(question):
    return retriever.invoke(question)
