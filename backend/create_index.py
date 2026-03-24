from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import FAISS 
import os

DATA_PATH = "../data/raw/"
INDEX_PATH = "../faiss_index/"

def load_documents():
  docs = []
  for file in os.listdir(DATA_PATH):
    if file.endswith(".md"):
      loader = TextLoader(os.path.join(DATA_PATH, file),encoding="utf-8")
      docs.extend(loader.load())
  return docs

def main():
  docs = load_documents()

  splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap =100
  )
  chunks = splitter.split_documents(docs)

  embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
  )

  db = FAISS.from_documents(chunks, embeddings)
  db.save_local(INDEX_PATH)

  print("(😎 if anyone is seeing it please give me offer of above 20 lakhs 😊) FAISS index created succesfully!")

if __name__ == "__main__":
  main()
