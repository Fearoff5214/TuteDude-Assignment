# Assignment 29: Q&A Chatbot Application (Cloud LLM & Ollama)


This project implements a Question & Answer chatbot using LangChain with two different Large Language Models:

- Cloud LLM (Groq)
- Ollama (Local Llama 3)

The application allows users to switch between a cloud-based model and a locally running open-source model through a simple Streamlit interface.

Tech Stack

- Python
- LangChain
- Streamlit
- Groq API
- Ollama
- Llama 3
- Python Dotenv


2. Install dependencies

pip install -r requirements.txt

Configure Environment Variables

Create a .env file.

GROQ_API_KEY=your_api_key

Setup Ollama

Download and install Ollama.

first pull the Llama 3 model.

ollama pull llama3

Ensure Ollama is running before using the local model.

Run the Application

python -m streamlit run app.py

The application will opened at this web address after running the above command:    


http://localhost:8501


Usage

1. Launch the application.
2. Select a model:
   - Cloud Model
   - Ollama
3. Enter a question.
4. Click **Ask**.
5. View the generated response.


Sample Questions to test the model

- What is Artificial Intelligence?
- Explain Machine Learning.
- What is LangChain?
- Difference between CNN and RNN.
- What is Generative AI?

Concepts Learned

- LangChain Prompt Templates
- Cloud-based LLM Integration
- Local LLM using Ollama
- Model Switching
- Streamlit Application Development
