import tempfile
import streamlit as st

from rag import build_vectorstore, get_answer

st.set_page_config(page_title="ChatGroq RAG",page_icon="📄",)

st.title("📄 ChatGroq RAG Chatbot")
st.caption("Upload a PDF and ask questions about its content.")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "retriever" not in st.session_state:
    st.session_state.retriever = None
uploaded_pdf = st.file_uploader("Choose a PDF document",type="pdf")

if uploaded_pdf is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_pdf.read())
        pdf_path = temp_file.name

    if st.button("Process Document"):
        with st.spinner("Reading the document and creating embeddings..."):
            try:
                st.session_state.retriever = build_vectorstore(pdf_path)
                st.success("Your document is ready! You can start asking questions.")
            except Exception as e:
                st.error(f"Something went wrong:\n{e}")

for chat in st.session_state.messages:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

user_question = st.chat_input("Ask something about the uploaded PDF...")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("user"):
        st.write(user_question)

    if st.session_state.retriever is None:
        response = "📄 Please upload and process a PDF before asking questions."
    else:
        with st.spinner("Thinking..."):
            response = get_answer(user_question,st.session_state.retriever)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
