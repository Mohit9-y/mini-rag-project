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
            st.sidebar.warning("⚠️ Backend is starting up. This can take ~ 60s.")
            time.sleep(5)
            st.rerun()
else:
    st.sidebar.success("✅ Connected to Render")


query = st.text_input(
    "Ask anything:", 
    placeholder="Ask anything related to Indecimal...",
    disabled=not st.session_state.backend_ready
)

if query:
    if st.session_state.backend_ready:
        with st.spinner("Searching and generating answer..."):
            try:
                res = requests.get(f"{BACKEND_URL}/ask", params={"query": query})
                if res.status_code == 200:
                    data = res.json()

                    answer = data.get("answer", "No answer found.")
                    sources = data.get("context", [])
                    st.subheader("Answer:")
                    st.markdown(answer)
                    with st.expander("📚 View Reference Sources"):
                        for i, doc in enumerate(sources):
                            st.info(f"Source {i+1}:\n{doc}")
                else:
                    st.error(f"Error: {res.status_code}. Backend might be overloaded.")
            except Exception as e:
                st.error("Connection lost. Please refresh.")
    else:
        st.warning("Please wait for the backend to connect.")