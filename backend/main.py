from fastapi import FastAPI
from rag_pipeline import ask_question

app = FastAPI()

@app.get("/ask")
def ask(query: str):
  result = ask_question(query)
  return result