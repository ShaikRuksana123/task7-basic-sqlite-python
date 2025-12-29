import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# CONNECT TO DATABASE
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")
conn.commit()

# INSERT DATA
cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Laptop', 2, 50000)")
cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Phone', 5, 20000)")
cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Tablet', 3, 15000)")
cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Laptop', 1, 50000)")
cursor.execute("INSERT INTO sales (product, quantity, price) VALUES ('Phone', 2, 20000)")
conn.commit()

# SQL QUERY
query = """
SELECT
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
"""

# LOAD INTO PANDAS
df = pd.read_sql_query(query, conn)

# PRINT RESULT
print("Sales Summary:")
print(df)

# BAR CHART
df.plot(kind='bar', x='product', y='total_revenue')
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# CLOSE CONNECTION
conn.close()
