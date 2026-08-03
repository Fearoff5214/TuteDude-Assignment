Assignment 37: PDF Query RAG using AstraDB

1. Overview

This project demonstrates a Retrieval-Augmented Generation (RAG) application using LangChain and DataStax AstraDB. The application loads a PDF, creates embeddings, stores them in AstraDB, and retrieves relevant information to answer user queries.

2. Technologies Used

- Python
- LangChain
- AstraDB (DataStax)
- HuggingFace Embeddings
- Groq LLM
- PyPDF
- Google Colab

3. Project Structure

A37_AstraDB_RAG/
│
├── A37_AstraDB_RAG.ipynb
├── DevAnand_Resume.pdf
├── README.md
└── requirements.txt

4. AstraDB Setup

1. Create an AstraDB Account

Visit to this website, sign up and then create the db
https://astra.datastax.com

Sign in using your Google or GitHub account.

2. Create a Vector Database

- Click Create Database.
- Enter a database name.
- Select Vector Database.
- Choose a cloud provider and region.
- Click Create.

Wait until the database status becomes Active.

3. Generate Credentials

Open your database and copy:

- API Endpoint
- Application Token

These credentials are required to connect LangChain with AstraDB.

5. Installation

Install the required libraries.


pip install langchain
pip install langchain-community
pip install langchain-astradb
pip install langchain-huggingface
pip install langchain-groq
pip install pypdf
pip install sentence-transformers

6. Workflow

1. Upload the PDF.
2. Load the PDF using PyPDFLoader.
3. Split the document into smaller chunks.
4. Generate embeddings using HuggingFace.
5. Store embeddings in AstraDB.
6. Retrieve relevant document chunks.
7. Generate answers using the Groq LLM.

7. Sample Questions

- What technical skills are mentioned?
- What projects are included?
- What certifications are listed?
- What programming languages are known?
- What is the candidate's education?

Out-of-Context Question

Question:
Who won the IPL 2025?

Expected Response:

I couldn't find this information in the uploaded PDF.

8. Observations

Why AstraDB?
During this assignment, I observed that AstraDB stores document embeddings in the cloud, unlike FAISS which stores them locally. This makes AstraDB suitable for production applications because the data remains available even after restarting the application

Session State
Session state is useful because it helps preserve user interactions. In a chat application, it can be used to maintain conversation history instead of starting a new conversation after every request

FAISS vs AstraDB
FAISS is a local vector database mainly used for development and testing. AstraDB is a managed cloud vector database that provides persistence and scalability, making it more suitable for real-world RAG applications

9. Conclusion

This project demonstrates how to build a simple RAG application using LangChain and AstraDB. It stores document embeddings in a cloud vector database and retrieves relevant information to generate accurate answers from the uploaded PDF.