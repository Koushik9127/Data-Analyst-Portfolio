# 03 – SQL Ecommerce Analysis

**Objective:**  
Analyze ecommerce sales data to discover top products and top countries by revenue using SQL queries and Python visualizations.

**Dataset:**  
- File: `data/ecommerce.csv`  
- Encoding: ISO-8859-1  

**Skills Demonstrated:**  
- SQL queries (GROUP BY, SUM, ORDER BY, LIMIT)  
- KPI calculation  
- Data visualization using Matplotlib  
- SQLite integration for querying  
- File handling and report generation  

## Project Structure

03-sql-ecommerce-analysis/
├── data/
│ └── ecommerce.csv
├── generate_results.py
├── reports/
│ ├── top_countries.csv
│ ├── top_products.csv
│ ├── top_countries.png
│ └── top_products.png
└── README.md

## Reports & Visualizations

- **Top 10 Countries by Revenue:** `reports/top_countries.png`  
- **Top 10 Products by Revenue:** `reports/top_products.png`  
- CSV files for further analysis: `reports/top_countries.csv`, `reports/top_products.csv`  

## How to Run

```bash
cd 03-sql-ecommerce-analysis
python3 generate_results.py
This will generate all reports and plots in the reports/ folder.
