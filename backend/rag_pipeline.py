import os
from langchain_huggingface import HuggingFaceEmbeddings
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpointEmbeddings


INDEX_PATH = "../faiss_index/"


embeddings = HuggingFaceEndpointEmbeddings(
    repo_id="sentence-transformers/all-MiniLM-L6-v2", 
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    task="feature-extraction" 
)

db = FAISS.load_local(
  INDEX_PATH,
   embeddings,
   allow_dangerous_deserialization=True
   )

llm = ChatOpenAI(
  model="nvidia/nemotron-3-nano-30b-a3b:free",
  openai_api_base="https://openrouter.ai/api/v1",
  openai_api_key=OPENROUTER_API_KEY,
  temperature=3
)

prompt_template = """
You are a helpful assistant.

Answer ONLY using the context below.
If the answer is not in the context, say:
"Answer not found in provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

prompt = PromptTemplate(
  template = prompt_template,
  input_variables = ["context", "question"]
)

def ask_question(query):
  docs = db.similarity_search(query, k =3)

  context = "\n\n".join([doc.page_content for doc in docs])

  final_prompt = prompt.format(context=context,question=query)

  response = llm.invoke(final_prompt)
  answer = response.content 

  return {
    "answer": answer,
    "context": [doc.page_content for doc in docs]
  }
