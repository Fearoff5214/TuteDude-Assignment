# Assignment 39 - GenAI Application Deployment

This assignment demonstrates the deployment of my CodeLlama Coding Assistant on cloud platforms.

## Project Features

- Generate Python code
- Explain Python code
- Debug Python code
- Optimize Python code

## Technologies Used

- Python
- Streamlit
- Ollama (Local Development)
- Groq API (Cloud Deployment)
- LangChain
- CodeLlama
- Llama 3.3 70B Versatile

---

## GitHub Repository

Repository Link:

https://github.com/DEVANAND-JAYARAMAN/GenAI-Asssignements-TuteDude/

---

## Streamlit Community Cloud Deployment

Live Application:

https://codellama-with-ollama.streamlit.app/

### Deployment Steps

1. Created a GitHub repository and pushed the project.
2. Logged into Streamlit Community Cloud.
3. Connected the GitHub repository.
4. Selected `app.py` as the main application.
5. Added the `GROQ_API_KEY` inside Streamlit Secrets.
6. Deployed the application successfully.
7. Tested all the features after deployment.

---

## Hugging Face Spaces

Space Link:

https://huggingface.co/spaces/devanand170904/CodeLlama-Ollama-Assistant

### Deployment Steps

1. Created a new Hugging Face Space.
2. Uploaded the required project files.
3. Configured the README file.
4. Verified that the Space was created successfully.

---

## Running the Project Locally

Install the required packages

```bash
pip install -r requirements.txt
```

Start Ollama

```bash
ollama serve
```

Run the application

```bash
streamlit run app.py
```

---

## Cloud Deployment Note

The original application was developed using **Ollama** with the **CodeLlama** model for local execution.

Since Streamlit Community Cloud cannot run a local Ollama server, the deployed version was updated to use the **Groq API** with the **Llama 3.3 70B Versatile** model.

The application features remain the same after deployment.

- Generate Code
- Explain Code
- Debug Code
- Optimize Code


## Deployment Observation

I successfully deployed the application on Streamlit Community Cloud and verified that all features were working correctly.

I also created a Hugging Face Space and uploaded the project files. This assignment helped me understand the deployment workflow, GitHub integration, secret management, and the differences between local and cloud-based LLM deployment