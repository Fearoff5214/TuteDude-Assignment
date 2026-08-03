import streamlit as st
from chatbot import get_answer

st.set_page_config(page_title="Q&A Chatbot")
st.title("Q&A Chatbot")
model = st.selectbox("Choose Model",["Cloud Model", "Ollama"])
question = st.text_input("Ask a question")
if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")

    else:
        with st.spinner("Generating response..."):
            try:
                answer = get_answer(question, model)
                st.success("Response Generated")
                st.write(answer)
            except Exception as e:
                st.error(str(e))