#Task 4: Create SQLAlchemy Engine

from sqlalchemy import create_engine, inspect

engine = create_engine("sqlite:///company.db")

inspector = inspect(engine)

print("Connected Successfully!\n")
print("Available Tables:")
print(inspector.get_table_names())