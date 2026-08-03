import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent

load_dotenv()
# Connect to SQLite database
db = SQLDatabase.from_uri("sqlite:///company.db")

# Loading the Groq LLM from the env variable
llm = ChatGroq(model="llama-3.1-8b-instant",api_key=os.getenv("GROQ_API_KEY"))
# Createng the toolkit
toolkit = SQLDatabaseToolkit(db=db,llm=llm)

# Creating theSQL Agent
agent = create_sql_agent(llm=llm,toolkit=toolkit,verbose=True, agent_executor_kwargs={"handle_parsing_errors": True})
print("SQL Agent Created Successfully!")

questions = ["How many employees are there in each department?","Who has the highest salary?",
    "What is the total sales amount?","What is the average salary per department?",
    "List all employees in the IT department.","Which employee made the highest sales?"]

for q in questions:
    print("\n" + "=" * 60)
    print("Question:", q)
    print("=" * 60)
    response = agent.invoke({"input": q})
    print("\nAnswer:")
    print(response["output"])

#task 9 - giving the ambiguous querry
response1 = agent.invoke({"input": "Show me sales"})
print(response1["output"])
response2 = agent.invoke({"input": "Who earns the most?"})
print(response2["output"])

