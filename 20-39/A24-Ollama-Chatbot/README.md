# Assignment 24 - Ollama Chatbot

## Technologies Used

- Python
- Ollama
- LangChain
- LangSmith
- Llama 3.2

## How to Run

1. Install Ollama from https://ollama.com
2. Pull the model:

ollama pull llama3.2

install the required packages using this command:

pip install langchain langchain-community langchain-ollama langsmith

open the python ipynb notebook and press the "run all cells" button

it will run all the cells and check the traces in the LangSmith dashboard

Output is that the local chatbot response generated using Ollama and LangSmith trace showing model execution

this is my cmd commands and output:

 ollama --version
ollama version is 0.31.2
PS C:\Users\DS> ollama list
NAME                       ID              SIZE      MODIFIED
nomic-embed-text:latest    0a109f422b47    274 MB    About an hour ago
PS C:\Users\DS> ollama pull llama3.2
pulling manifest
pulling dde5aa3fc5ff: 100% ▕███████████████████████████████████████████████████████████████████████▏ 2.0 GB
pulling 966de95ca8a6: 100% ▕███████████████████████████████████████████████████████████████████████▏ 1.4 KB
pulling fcc5a6bec9da: 100% ▕███████████████████████████████████████████████████████████████████████▏ 7.7 KB
pulling a70ff7e570d9: 100% ▕███████████████████████████████████████████████████████████████████████▏ 6.0 KB
pulling 56bb8bd477a5: 100% ▕███████████████████████████████████████████████████████████████████████▏   96 B
pulling 34bb5ab01051: 100% ▕███████████████████████████████████████████████████████████████████████▏  561 B
verifying sha256 digest
writing manifest
success
PS C:\Users\DS> ollama list
NAME                       ID              SIZE      MODIFIED
llama3.2:latest            a80c4f17acd5    2.0 GB    15 seconds ago
nomic-embed-text:latest    0a109f422b47    274 MB    About an hour ago

I created the api key in langchain and i put that in the env file and now im not including the env file to secure my api key
