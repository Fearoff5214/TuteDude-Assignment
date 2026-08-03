from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant. Answer ONLY from the given context. If the answer is not available in the context,
reply with
"I couldn't find this information in the uploaded document."

Context:{context}
Question:{question}""")