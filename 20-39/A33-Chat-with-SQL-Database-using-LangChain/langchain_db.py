from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///company.db")
print("Available Tables:")
print(db.get_usable_table_names())
print("\nSchema Information:\n")
print(db.get_table_info())