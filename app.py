import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

st.title("RAG Application with Llama2")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
if uploaded_file:
    try:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getvalue())
        
        loader = PyPDFLoader("temp.pdf")
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents)
        
        embeddings = OllamaEmbeddings(model="llama2")
        vectorstore = DocArrayInMemorySearch.from_documents(docs, embedding=embeddings)
        
        llm = Ollama(model="llama2")
        qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever())
        
        query = st.text_input("Ask a question about the PDF:")
        if query:
            result = qa_chain.run(query)
            st.write("Answer:", result)
    except Exception as e:
        st.error(f"Error processing PDF: {str(e)}")
    finally:
        if os.path.exists("temp.pdf"):
            os.remove("temp.pdf")
