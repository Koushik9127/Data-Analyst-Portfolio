import pandas as pd
import matplotlib.pyplot as plt
import os
import sqlite3

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

# Load dataset with encoding fix
df = pd.read_csv("data/ecommerce.csv", encoding="ISO-8859-1")

# Create SQLite DB
conn = sqlite3.connect("03-sql-ecommerce-analysis.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

# SQL Queries
query1 = "SELECT Country, SUM(Quantity*UnitPrice) as Revenue FROM sales GROUP BY Country ORDER BY Revenue DESC LIMIT 10"
top_countries = pd.read_sql(query1, conn)

query2 = "SELECT StockCode, Description, SUM(Quantity*UnitPrice) as Revenue FROM sales GROUP BY StockCode ORDER BY Revenue DESC LIMIT 10"
top_products = pd.read_sql(query2, conn)

# Save reports
top_countries.to_csv("reports/top_countries.csv", index=False)
top_products.to_csv("reports/top_products.csv", index=False)

# Plotting top 10 countries
plt.figure(figsize=(8,5))
plt.bar(top_countries['Country'], top_countries['Revenue'], color='teal')
plt.xticks(rotation=45)
plt.title("Top 10 Countries by Revenue")
plt.tight_layout()
plt.savefig("reports/top_countries.png")
plt.close()

# Plotting top 10 products
plt.figure(figsize=(8,5))
plt.bar(top_products['Description'], top_products['Revenue'], color='orange')
plt.xticks(rotation=90)
plt.title("Top 10 Products by Revenue")
plt.tight_layout()
plt.savefig("reports/top_products.png")
plt.close()

print("SQL Ecommerce Analysis reports generated successfully!")
