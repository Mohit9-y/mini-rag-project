from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Backend is running"}

@app.get("/ask")
def ask(query: str):
    # Move the heavy import INSIDE the function
    from rag_pipeline import ask_question
    return ask_question(query)