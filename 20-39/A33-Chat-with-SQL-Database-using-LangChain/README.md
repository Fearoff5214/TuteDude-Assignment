A33 - Chat with SQL Database using LangChain

Build a LangChain SQL Agent that interacts with SQLite and MySQL databases using natural language.

Technologies Used
- Python
- SQLite
- MySQL
- SQLAlchemy
- LangChain
- Groq
- Python-dotenv

Features
- SQLite database creation
- MySQL database connection
- SQLAlchemy integration
- LangChain SQLDatabase
- SQL Agent
- Natural language to SQL
- Dynamic SQL query execution


pip install -r requirements.txt

4. Create a .env file

GROQ_API_KEY=your_api_key

5. Run
python sql_agent.py

Sample Questions

- How many employees are there in each department?
- Who has the highest salary?
- What is the total sales amount?
- What is the average salary per department?

iv addded the screenshots of the mysql workbench and then I intruppted the kernel while running the jupiter file sometimes. 

install these verions inorder to run the file successfully without any errors

"pip install langchain==0.3.27 langchain-community==0.3.27 langchain-groq==0.3.7 sqlalchemy==2.0.41 python-dotenv==1.1.1 pymysql==1.1.1"


