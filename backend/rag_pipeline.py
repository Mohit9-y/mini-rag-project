from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

INDEX_PATH = "../faiss_index/"

embeddings = HuggingFaceEmbeddings(
  model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(INDEX_PATH, embeddings)

llm = ChatOpenAI(
  model="meta-llama/llama-3.3-70b-instruct:free",
  openai_api_base="https://openrouter.ai/api/v1",
  openai_api_key=os.getenv("OPENROUTER_API_KEY"),
  temperature=0
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

  answer = llm.predict(final_prompt)

  return {
    "answer": answer,
    "context": [doc.page_content for doc in docs]
  }
