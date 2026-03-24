import streamlit as st
import requests

st.title("Indecimal RAG Chatbot")

query = st.text_input("Ask a question:")

if st.button("Ask"):
  if query:      
    res = requests.get(f"http://127.0.0.1:8000/ask?query={query}")
    if res.status_code == 200:
      data = res.json()

      st.subheader("Answer:")
      st.write(data["answer"])

      st.subheader("Retrieved Context:")
      for i, chunk in enumerate(data["context"]):
        st.write(f"{i+1}. {chunk}")

  else:
    st.error(f"Backend Error {res.status_code}")
    st.write("Response text from backend:", res.text)