This assignment implements the chatbot option. The RAG section is optional according to the assignment and has been intentionally omitted

# Assignment 26 - Groq API Chatbot & FastAPI

Features

- Groq API integration
- Chatbot using Llama 3.3 70B Versatile
- FastAPI REST API
- Health check endpoint
- Chat endpoint
- Environment variable support
- Basic logging

API Endpoints

GET /

Returns a welcome message.

GET /health

Checks whether the API is running.

POST /chat

Accepts a user query and returns a response from the Groq model.

Example request:

{
  "query": "What is Artificial Intelligence?"
}

Technologies Used

- Python
- Groq API
- FastAPI
- Pydantic
- Python Dotenv

run the main.go file with the help of this command:

python -m uvicorn main:app --reload