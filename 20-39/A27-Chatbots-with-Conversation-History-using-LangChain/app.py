import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Page title
st.set_page_config(page_title="Stateful Chatbot", page_icon="🤖")
st.title("🤖 Stateful Chatbot using LangChain & Groq")
# Load API Key
groq_api_key = st.secrets["GROQ_API_KEY"]
# Load LLM
llm = ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key,temperature=0)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([("system", "You are a helpful AI assistant."),MessagesPlaceholder(variable_name="chat_history"),("human", "{question}")])

chain = prompt | llm
# Initialize history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
MAX_MESSAGES = 6
# Display previous messages
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    else:
        with st.chat_message("assistant"):
            st.write(msg.content)

# Chat input
question = st.chat_input("Ask something...")
if question:
    # Show user message
    with st.chat_message("user"):
        st.write(question)
    # Save user message
    st.session_state.chat_history.append(HumanMessage(content=question))

    # Trim history
    if len(st.session_state.chat_history) > MAX_MESSAGES:
        st.session_state.chat_history = st.session_state.chat_history[-MAX_MESSAGES:]

    # Generate response
    response = chain.invoke({"chat_history": st.session_state.chat_history,"question": question})

    # Show AI response
    with st.chat_message("assistant"):
        st.write(response.content)

    # Save AI response
    st.session_state.chat_history.append(
        AIMessage(content=response.content))
    # Trim again
    if len(st.session_state.chat_history) > MAX_MESSAGES:
        st.session_state.chat_history = st.session_state.chat_history[-MAX_MESSAGES:]