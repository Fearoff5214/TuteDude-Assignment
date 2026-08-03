from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [("system","You are a helpful AI assistant. Answer clearly and politely."),
        ("human","{question}")])