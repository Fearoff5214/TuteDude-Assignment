# ChatGroq RAG Application with Streamlit UI
Features

- Upload PDF documents
- Automatic document chunking
- Semantic search using vector embeddings
- Fast response generation using ChatGroq
- Interactive Streamlit chat interface
- Conversation history using Streamlit Session State
- Grounded answers based on uploaded documents
- Graceful handling of out-of-context questions

Tech Stack

- Python
- Streamlit
- LangChain
- ChatGroq
- Ollama Embeddings
- FAISS Vector Store
- PyPDF Loader

Create Virtual Environment

python -m venv venv
venv\Scripts\activate


Install Dependencies

pip install -r requirements.txt

Configure Environment Variables

Create a .env file in the project root.


GROQ_API_KEY=your_groq_api_key

Install Ollama

Download and install Ollama from:

https://ollama.com/download

Pull the embedding model:

ollama pull nomic-embed-text

Make sure the Ollama service is running before launching the application.

Run the Application

python -m streamlit run app.py

Open your browser and visit the address after running the above command:

http://localhost:8501

Workflow

1. Upload a PDF document.
2. Load and split the document into chunks.
3. Generate embeddings using Ollama Embeddings.
4. Store document embeddings in a FAISS vector database.
5. Ask questions related to the uploaded document.
6. Retrieve relevant document chunks.
7. Generate grounded answers using ChatGroq.
8. Display responses in the Streamlit chat interface.

Sample Questions

- What is the document about?
- Summarize the first chapter.
- Explain the key concepts discussed.
- What are the conclusions?
- Give a brief overview of the document.

Testing

Test Case 1

Ask a factual question directly related to the uploaded document.

Test Case 2

Ask a follow-up question to verify conversation continuity.

Test Case 3

Ask an unrelated question to verify that the chatbot responds appropriately when the answer is not found in the uploaded document

go to this website https://console.groq.com/keys and I already pasted the image for the proof of groq api key getting
to create the new api key, go to that website and click the create new api key. and then give the token name and description and then make the api. dont share the api publically.