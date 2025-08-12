# 📚 RAG-Based AI Assistant

This project is a Retrieval-Augmented Generation (RAG) AI Assistant that answers user questions using information from custom documents.  
It combines Large Language Models (LLMs) with a vector database to give accurate, context-based answers.

---

## 🚀 Features
- Upload PDF, text, or knowledge base documents  
- Stores document data in a FAISS Vector Database for quick search  
- Integrates with LangChain and an LLM like OpenAI GPT  
- Answers are based only on the uploaded documents  
- Works for domain-specific topics such as technical guides, research, or policies  

---

## 🛠️ Tech Stack
- Python  
- LangChain  
- OpenAI API or other LLM provider  
- FAISS (Vector Search)  
- Streamlit for the interface  
- AWS S3 or EC2 for hosting (optional)  

---

## ⚙️ How It Works
1. Document upload → user provides one or more documents  
2. Text processing → splits content into chunks and creates embeddings  
3. Vector storage → saves embeddings in FAISS for fast retrieval  
4. Query handling → finds the most relevant text chunks for a question  
5. Answer generation → the LLM uses the retrieved data to generate a response  

---

## 🎯 Use Cases
- Company knowledge base chatbot  
- Academic research assistant  
- Automated customer support  
- Legal or policy document search  

---

## 📌 Demo
Add link to live demo or screenshots here  

---

Author: Y sree Ranga Rohith
Contact: rohithroyal001@gmail.com
