import tempfile
import streamlit as st

from rag import build_vectorstore, get_answer

# Page Configuration using this
st.set_page_config(page_title="ChatGroq RAG",page_icon="📄",)

st.title("📄 ChatGroq RAG Chatbot")
st.caption("Upload a PDF and ask questions about its content.")

# Session State management is implemented hree to maintain the historry
if "messages" not in st.session_state:
    st.session_state.messages = []
if "retriever" not in st.session_state:
    st.session_state.retriever = None
# Upload PDF logic here comes
uploaded_pdf = st.file_uploader("Choose a PDF document",type="pdf")

if uploaded_pdf is not None:
    # Save uploaded PDF temporarily
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

# Chat History
for chat in st.session_state.messages:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

# User Input
user_question = st.chat_input("Ask something about the uploaded PDF...")

if user_question:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("user"):
        st.write(user_question)

    # Generate response
    if st.session_state.retriever is None:
        response = "📄 Please upload and process a PDF before asking questions."
    else:
        with st.spinner("Thinking..."):
            response = get_answer(user_question,st.session_state.retriever)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
