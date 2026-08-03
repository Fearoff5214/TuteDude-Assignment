import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit

load_dotenv()
# Load database
db = SQLDatabase.from_uri("sqlite:///company.db")
# Load LLM
llm = ChatGroq(model="llama3-8b-8192",api_key=os.getenv("GROQ_API_KEY"))

# Create Toolkit
toolkit = SQLDatabaseToolkit(db=db,llm=llm)

print("Toolkit Created Successfully!\n")
print("Available Tools:\n")
for tool in toolkit.get_tools():
    print(tool.name)