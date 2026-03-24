from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import os

DATA_PATH = "../data/raw/"
INDEX_PATH = "../faiss_index/"

def load_documents():
  docs = []
  for file in os.listdir(DATA_PATH):
    if file.endswith(".pdf"):
      loader = PyPDFLoader(os.path.join(DATA_PATH, file))
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
