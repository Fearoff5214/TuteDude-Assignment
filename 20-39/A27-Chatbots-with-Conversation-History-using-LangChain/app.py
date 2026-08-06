import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

st.set_page_config(page_title="Stateful Chatbot", page_icon="🤖")
st.title("🤖 Stateful Chatbot using LangChain & Groq")
groq_api_key = st.secrets["GROQ_API_KEY"]
llm = ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key,temperature=0)

prompt = ChatPromptTemplate.from_messages([("system", "You are a helpful AI assistant."),MessagesPlaceholder(variable_name="chat_history"),("human", "{question}")])

chain = prompt | llm
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
MAX_MESSAGES = 6
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    else:
        with st.chat_message("assistant"):
            st.write(msg.content)

question = st.chat_input("Ask something...")
if question:
    with st.chat_message("user"):
        st.write(question)
    st.session_state.chat_history.append(HumanMessage(content=question))

    if len(st.session_state.chat_history) > MAX_MESSAGES:
        st.session_state.chat_history = st.session_state.chat_history[-MAX_MESSAGES:]

    response = chain.invoke({"chat_history": st.session_state.chat_history,"question": question})

    with st.chat_message("assistant"):
        st.write(response.content)

    st.session_state.chat_history.append(
        AIMessage(content=response.content))
    if len(st.session_state.chat_history) > MAX_MESSAGES:
        st.session_state.chat_history = st.session_state.chat_history[-MAX_MESSAGES:]