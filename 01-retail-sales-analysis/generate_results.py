import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style('whitegrid')
os.makedirs('reports', exist_ok=True)

df = pd.read_csv('data/online_retail.csv', encoding='unicode_escape')
df = df.drop_duplicates()
df = df[df['Quantity'] > 0]
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True)
df['Total'] = df['Quantity'] * df['UnitPrice']

# KPIs
total_revenue = df['Total'].sum()
total_orders = df['InvoiceNo'].nunique()
avg_order_value = total_revenue / total_orders

with open('reports/kpis.txt', 'w') as f:
    f.write(f"Total revenue: ${total_revenue:,.2f}\n")
    f.write(f"Total orders: {total_orders}\n")
    f.write(f"Average order value: ${avg_order_value:,.2f}\n")

# Top 10 products
top_products = df.groupby('Description')['Total'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
top_products.plot(kind='barh', color='teal')
plt.title('Top 10 Products by Revenue')
plt.gca().invert_yaxis()
plt.savefig('reports/top_products.png')
plt.close()

# Top 10 countries
top_countries = df.groupby('Country')['Total'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
top_countries.plot(kind='bar', color='orange')
plt.title('Top 10 Countries by Revenue')
plt.ylabel('Revenue')
plt.savefig('reports/top_countries.png')
plt.close()

# Monthly sales trend
monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M'))['Total'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()
plt.figure(figsize=(12,6))
monthly_sales.plot(marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.ylabel('Revenue')
plt.savefig('reports/monthly_sales.png')
plt.close()
