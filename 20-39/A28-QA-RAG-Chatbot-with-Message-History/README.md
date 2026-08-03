# Assignment 28 - Q&A RAG Chatbot with Message History

Document Used

**Document:** DevAnand_Resume.pdf

The resume contains information about education, work experience, projects, technical skills, certifications, and achievements. It is used as the knowledge source for the chatbot.

Technologies Used

- Python
- LangChain
- HuggingFace Embeddings
- FAISS
- Groq (Llama 3.3 70B Versatile)
- PyPDF
- Sentence Transformers

Tasks Completed

Part 1 - Document Ingestion

- Loaded PDF using PyPDFLoader
- Displayed sample content
- Split the document using RecursiveCharacterTextSplitter

Part 2 - Vector Store

- Generated embeddings using HuggingFace Embeddings
- Stored embeddings in FAISS
- Created a retriever for similarity search

Part 3 - Prompt Engineering

- Created a ChatPromptTemplate
- Added system instructions
- Used MessagesPlaceholder for chat history

Part 4 - Conversational RAG

- Built a RAG pipeline
- Maintained conversation history
- Implemented history trimming

Part 5 - Testing

Tested the chatbot with multiple questions, including follow-up questions, and verified that responses were generated from the document context.

How to Run

1. Install the required libraries.

pip install -r requirements.txt


2. Place the PDF file in the project folder.
3. Open the notebook.
4. Enter your Groq API Key when prompted.
5. Run all notebook cells from top to bottom.
6. Start asking questions to the chatbot.

Sample Questions

- What projects has Dev Anand worked on?
- Tell me about VisionChallan AI.
- What certifications does Dev Anand have?
- What technical skills are listed?
- Explain the previous answer.


Conclusion

This project demonstrates a complete conversational RAG chatbot using LangChain, FAISS, HuggingFace Embeddings, and Groq. The chatbot retrieves information from documents, remembers previous conversations, and answers follow-up questions based on the retrieved context


I stored the groq api in the colab secrets and im not gonna pass this as a file as it will put me in danger
sharing the env variables and values in high risk and im not sharing it now. let me give how the env should look like
