import streamlit as st
from langchain_groq import ChatGroq

# page setup
st.set_page_config(page_title="Code Assistant",layout="wide")

st.title("💻 Code Assistant")
st.write("Generate, explain, debug and optimize Python code.")

# load groq model
llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=st.secrets["GROQ_API_KEY"],temperature=0.2)

# task selection
task = st.selectbox("Select Task",("Generate Code","Explain Code","Debug Code","Optimize Code"))
# user input
user_input = st.text_area("Enter your prompt or code",height=250)

# prompt templates
prompts = {
    "Generate Code":
f"""
Write Python code for the following requirement.

Requirement:
{user_input}

Return only the Python code with short comments.
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

Return:
1. Problems
2. Corrected code
3. Explanation
""",

    "Optimize Code":
f"""
Improve the following Python code.

Code:
{user_input}

Make it:
- More readable
- Faster if possible
- Follow Python best practices

Return the improved code.
"""}

# function to get response
def get_response(prompt):
    response = llm.invoke(prompt)
    return response.content

if st.button("Generate Response", use_container_width=True):
    if user_input.strip() == "":
        st.warning("Please enter a prompt or code.")
    else:
        with st.spinner("Generating response..."):
            result = get_response(prompts[task])
        st.subheader("Response")
        if task == "Generate Code":
            st.code(result, language="python")
        else:
            st.markdown(result)
st.markdown("---")
st.caption("Built using Streamlit and Groq Llama 3.3")