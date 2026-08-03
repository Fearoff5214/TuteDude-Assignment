import os

from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from prompts import prompt

llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0)
embedding = OllamaEmbeddings(model="nomic-embed-text")

def build_vectorstore(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    vectorstore = FAISS.from_documents(chunks,embedding)
    return vectorstore.as_retriever()

def get_answer(question, retriever):
    docs = retriever.invoke(question)
    context = "\n\n".join(
        doc.page_content
        for doc in docs)
    chain = prompt | llm
    response = chain.invoke({"context": context,"question": question})
    return response.content


#studied from both chatgpt and stackoverflow that using the functuon will help to get the answer from retreiver
#and it will be easy to maintain the code