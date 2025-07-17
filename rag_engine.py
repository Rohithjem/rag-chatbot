import fitz  # PyMuPDF

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# 1. Read and extract text from the uploaded PDF
def load_pdf_text(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

# 2. Create RAG pipeline: embed, store, and create retriever + LLM chain
def generate_rag_chain(text):
    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    # Embed text
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(chunks, embeddings)

    # Create retriever
    retriever = vectorstore.as_retriever(search_type="similarity", k=3)

    # Connect retriever with OpenAI model
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    return qa_chain
