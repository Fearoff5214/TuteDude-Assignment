#Task 3: Verify the Database

import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()
print("Employees")
print("-" * 40)
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

print("\nSales")
print("-" * 40)
cursor.execute("SELECT * FROM sales")
for row in cursor.fetchall():
    print(row)
conn.close()


#after running this file. it will print all the data that is present in the database