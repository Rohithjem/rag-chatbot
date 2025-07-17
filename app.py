import streamlit as st
from dotenv import load_dotenv
import os

from rag_engine import load_pdf_text, generate_rag_chain

# Load environment variables (for OpenAI API key)
load_dotenv()

st.set_page_config(page_title="RAG Document Chatbot 🤖", layout="wide")
st.title("📄 RAG-Based Document Q&A Chatbot")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file:
    with st.spinner("Reading and processing the document..."):
        # Extract text
        text = load_pdf_text(uploaded_file)

        # Build the RAG QA system
        qa_chain = generate_rag_chain(text)
        st.success("Document processed! You can now ask questions below.")

    # Input question
    query = st.text_input("❓ Ask a question based on the document:")

    if query:
        with st.spinner("Generating answer..."):
            response = qa_chain.run(query)
            st.markdown("**Answer:**")
            st.write(response)
