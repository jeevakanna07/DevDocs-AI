import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag import answer_question


app = FastAPI(
    title="DevDocs AI",
    description="Developer Documentation RAG Assistant",
    version="1.0.0"
)


# CORS configuration
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    os.getenv(
        "FRONTEND_URL",
        "https://YOUR_USERNAME.github.io"
    )
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "DevDocs AI API is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    result = answer_question(request.question)

    return result