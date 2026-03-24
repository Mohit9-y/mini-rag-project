import streamlit as st
import requests
import os
import time

BACKEND_URL = st.secrets.get("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="AI RAG Assistant", page_icon="🤖")
st.title("🤖 Personal AI Assistant")


def check_backend():
    try:
        response = requests.get(f"{BACKEND_URL}/", timeout=5)
        return response.status_code == 200
    except:
        return False

st.sidebar.header("System Status")
if "backend_ready" not in st.session_state:
    st.session_state.backend_ready = False

if not st.session_state.backend_ready:
    with st.sidebar.status("Connecting to Backend...", expanded=True) as status:
        if check_backend():
            st.session_state.backend_ready = True
            status.update(label="✅ Backend Online", state="complete")
        else:
            st.write("Checking if server is awake...")
            st.sidebar.warning("⚠️ Backend is starting up. This can take 60s on the free tier.")
            time.sleep(10)
            st.rerun()
else:
    st.sidebar.success("✅ Connected to Render")


query = st.text_input(
    "Ask a question about your documents:", 
    placeholder="e.g., What is the project about?",
    disabled=not st.session_state.backend_ready
)

if query:
    if st.session_state.backend_ready:
        with st.spinner("Searching and generating answer..."):
            try:
                res = requests.get(f"{BACKEND_URL}/ask", params={"query": query})
                if res.status_code == 200:
                    st.markdown(f"### Answer:\n{res.json()}")
                else:
                    st.error(f"Error: {res.status_code}. Backend might be overloaded.")
            except Exception as e:
                st.error("Connection lost. Please refresh.")
    else:
        st.warning("Please wait for the backend to connect.")