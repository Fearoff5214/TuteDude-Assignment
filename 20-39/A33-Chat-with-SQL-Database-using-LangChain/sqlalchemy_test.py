#Task 4: Create SQLAlchemy Engine

#first we can install all the dependency needed to run this file

from sqlalchemy import create_engine, inspect

# Create SQLAlchemy engine
engine = create_engine("sqlite:///company.db")

# Inspect the database first
inspector = inspect(engine)

print("Connected Successfully!\n")
print("Available Tables:")
print(inspector.get_table_names())