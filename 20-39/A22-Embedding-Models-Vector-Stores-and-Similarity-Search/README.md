##The OpenAI embedding task could not be completed because the API limit was reached. Instead, Hugging Face embeddings were used to show the same workflow

I can add the image of that for the proof, I searched this on Google and found that instead of this, I can continue with the Huggin Face embeddings

In this assignment, I explored embedding models, vector stores, and semantic similarity search using LangChain. I generated embeddings with the Hugging Face embedding model, stored them in FAISS and ChromaDB, and performed similarity searches on document chunks. This workflow provides the retrieval foundation required for building Retrieval-Augmented Generation (RAG) applications

So I downloaded the ollama from google and ran these commands to downlaod the embedding model
"ollama pull nomic-embed-text"

to check i used the command:

ollama list

and I ran the task 6 in vs code by using this command:

python task6_ollama.py

