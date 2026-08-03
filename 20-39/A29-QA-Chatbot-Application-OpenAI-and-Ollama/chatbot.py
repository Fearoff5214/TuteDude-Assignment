import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from prompts import prompt
load_dotenv()

def get_answer(question, model_type):

    print("=" * 50)
    print("Model Selected :", model_type)
    print("Question :", question)

    if model_type == "Cloud Model":
        print("Creating Groq Model...")
        llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"),model="llama-3.3-70b-versatile",temperature=0)

    else:
        print("Creating Ollama Model...")
        llm = ChatOllama(model="llama3")

    print("Building Chain...")
    chain = prompt | llm
    print("Invoking Model...")
    response = chain.invoke({"question": question})
    print("Finished!")
    return response.content