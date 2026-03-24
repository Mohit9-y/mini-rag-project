import streamlit as st
import requests

st.title("Indecimal RAG Chatbot")

query = st.text_input("Ask a question:")

if st.button("Ask"):
  if query:      
    res = requests.get(f"http://localhost:8000/ask?query={query}")
    data = res.json()

    st.subheader("Answer:")
    st.write(data["answer"])

    st.subheader("Retrieved Context:")
    for i, chunk in enumerate(data["context"]):
      st.write(f"{i+1}. {chunk}")