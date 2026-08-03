import sqlite3
# Connect to SQLite database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY,name TEXT NOT NULL,department TEXT NOT NULL,salary INTEGER NOT NULL)""")

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (sale_id INTEGER PRIMARY KEY,employee_id INTEGER,amount INTEGER,sale_date TEXT,FOREIGN KEY(employee_id) REFERENCES employees(id))""")

#instead of putting every code in the db, we can directly write the python code and then If we run it, the databse will be created
# Insert employee data
employees = [(1, "Alice", "HR", 50000),  (2, "Bob", "IT", 70000),
    (3, "Charlie", "Finance", 65000),(4, "David", "IT", 80000),(5, "Eva", "HR", 55000),(6, "Frank", "Sales", 60000),
    (7, "Grace", "Sales", 62000),(8, "Henry", "Finance", 75000),(9, "Ivy", "Marketing", 58000),(10, "Jack", "Marketing", 61000)]
cursor.executemany("INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?)",employees)
# Insert sales data
sales = [(1, 6, 10000, "2025-01-10"),(2, 6, 15000, "2025-01-15"),(3, 7, 12000, "2025-02-01"),(4, 7, 18000, "2025-02-10"),
    (5, 2, 8000, "2025-03-05"),(6, 4, 11000, "2025-03-12"),
    (7, 8, 9000, "2025-04-01"),(8, 3, 7000, "2025-04-18"),(9, 9, 5000, "2025-05-10"),(10, 10, 6000, "2025-05-20")]

cursor.executemany("INSERT OR REPLACE INTO sales VALUES (?, ?, ?, ?)",sales)
#now all these data will be inserted into the databsase if we run this code using this command: python sqlite_setup.py
conn.commit()
print("Tables created successfully!")
conn.close()