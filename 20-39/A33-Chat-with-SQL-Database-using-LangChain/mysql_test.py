from langchain_community.utilities import SQLDatabase

mysql_uri = "mysql+pymysql://root:DEVJAYARAMAN@localhost/company"

mysql_db = SQLDatabase.from_uri(mysql_uri)
print("Connected Successfully!")
print(mysql_db.get_usable_table_names())