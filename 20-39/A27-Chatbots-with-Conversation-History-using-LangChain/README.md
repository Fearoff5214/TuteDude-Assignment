Assignment 27 - Chatbots with Conversation History using LangChain

This project demonstrates how to build a stateful chatbot using LangChain and Groq. The chatbot remembers previous conversations, trims old messages to manage context length, and answers follow-up questions based on conversation history.

Features

- ChatPromptTemplate
- MessagesPlaceholder
- Conversation History
- History Trimming
- Q&A Chatbot
- Stateful Streamlit Chatbot

Technologies Used

- Python
- Streamlit
- LangChain
- Groq

Model Used is

- llama-3.1-8b-instant

Run the Application

streamlit run app.py or uvicorn main:app --reload or python -m streamlit run app.py

what happened is that I created the file .env and thought that it will work, but i studied that while using the streamlit, we can use the command called """"st.secrets["GROQ_API_KEY"]""""

so I created the folder under streamlit and ran the application. I used the ChatGPT and stackoverflow to find and rectify the mistakes. Ive attached the screenshots of the frontend or streamlit. 

Now I am not sharing the groq api key as it is sensitive and I dont want to create the issue. let me put a summy variable in the line of actual value. Sensitive info should be carefully preserved right, so Im doing it..... 