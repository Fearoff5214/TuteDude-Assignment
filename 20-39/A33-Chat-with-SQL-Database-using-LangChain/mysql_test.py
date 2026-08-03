from langchain_community.utilities import SQLDatabase

# Replace with your MySQL username/password
mysql_uri = "mysql+pymysql://root:DEVJAYARAMAN@localhost/company"

mysql_db = SQLDatabase.from_uri(mysql_uri)
print("Connected Successfully!")
print(mysql_db.get_usable_table_names())