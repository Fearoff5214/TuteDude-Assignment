from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI(title="Groq Chatbot API")

class ChatRequest(BaseModel):
    query: str

def groq_chat(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system","content": "You are a helpful AI assistant."},{"role": "user","content": prompt}])
    return response.choices[0].message.content

@app.get("/")
def home():
    return {"message": "Welcome to Groq Chatbot API"}

@app.get("/health")
def health():
    return {"status": "API is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        answer = groq_chat(request.query)
        logging.info("Chat request processed successfully.")
        return {
            "answer": answer
        }

    except Exception as e:
        logging.error(str(e))
        return {
            "error": str(e)
        }