import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY,name TEXT NOT NULL,department TEXT NOT NULL,salary INTEGER NOT NULL)""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (sale_id INTEGER PRIMARY KEY,employee_id INTEGER,amount INTEGER,sale_date TEXT,FOREIGN KEY(employee_id) REFERENCES employees(id))""")

employees = [(1, "Alice", "HR", 50000),  (2, "Bob", "IT", 70000),
    (3, "Charlie", "Finance", 65000),(4, "David", "IT", 80000),(5, "Eva", "HR", 55000),(6, "Frank", "Sales", 60000),
    (7, "Grace", "Sales", 62000),(8, "Henry", "Finance", 75000),(9, "Ivy", "Marketing", 58000),(10, "Jack", "Marketing", 61000)]
cursor.executemany("INSERT OR REPLACE INTO employees VALUES (?, ?, ?, ?)",employees)
sales = [(1, 6, 10000, "2025-01-10"),(2, 6, 15000, "2025-01-15"),(3, 7, 12000, "2025-02-01"),(4, 7, 18000, "2025-02-10"),
    (5, 2, 8000, "2025-03-05"),(6, 4, 11000, "2025-03-12"),
    (7, 8, 9000, "2025-04-01"),(8, 3, 7000, "2025-04-18"),(9, 9, 5000, "2025-05-10"),(10, 10, 6000, "2025-05-20")]

cursor.executemany("INSERT OR REPLACE INTO sales VALUES (?, ?, ?, ?)",sales)
conn.commit()
print("Tables created successfully!")
conn.close()