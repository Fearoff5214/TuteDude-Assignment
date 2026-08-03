import streamlit as st
from langchain_ollama import ChatOllama

# Page setup using this code base
st.set_page_config(page_title="CodeLlama Assistant", page_icon="💻", layout="wide")
st.title("CodeLlama Coding Assistant")
st.write("Generate, explain, debug and optimize Python code using CodeLlama.")

# Load the model using this code base
llm = ChatOllama(model="codellama:7b", temperature=0.2)
st.success("CodeLlama model loaded successfully.")

# task selection
task = st.selectbox("Select Task",("Generate Code", "Explain Code", "Debug Code", "Optimize Code"))

# user to input something
user_input = st.text_area("Enter your prompt or code", height=250)

prompts = {
    "Generate Code":
    f"""
Write Python code for the following requirement.

Requirement:
{user_input}

Return clean Python code with short comments only.
""",
    "Explain Code":
    f"""
Explain the following Python code in simple language.

Code:
{user_input}

Explain it step by step.
""",

    "Debug Code":
    f"""
Find the errors in the following Python code.

Code:
{user_input}

Provide:
1. Issues found
2. Corrected code
3. Explanation
""",

    "Optimize Code":
    f"""
Optimize the following Python code.

Code:
{user_input}

Improve:
- Readability
- Performance
- Best Practices

Return the optimized code.
"""}

def get_response(prompt):
    response = llm.invoke(prompt)
    return response.content

if st.button("Generate Response"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt or code.")
    else:
        result = get_response(prompts[task])
        st.subheader("Response")
        if task == "Generate Code":
            st.code(result, language="python")
        else:
            st.markdown(result)