import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

os.makedirs("reports", exist_ok=True)

df = pd.read_csv("data/churn.csv")

# Clean numeric column
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna(subset=["TotalCharges"])

# KPIs
total_customers = len(df)
churned_customers = df[df["Churn"] == "Yes"].shape[0]
churn_rate = churned_customers / total_customers * 100
avg_tenure = df["tenure"].mean()

with open("reports/kpis.txt", "w") as f:
    f.write(f"Total Customers: {total_customers}\n")
    f.write(f"Churned Customers: {churned_customers}\n")
    f.write(f"Churn Rate: {churn_rate:.2f}%\n")
    f.write(f"Average Tenure: {avg_tenure:.2f} months\n")

# Churn distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.savefig("reports/churn_distribution.png")
plt.close()

# Tenure vs charges
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="tenure", y="MonthlyCharges", hue="Churn")
plt.title("Tenure vs Monthly Charges")
plt.savefig("reports/tenure_vs_monthly.png")
plt.close()

# Churn rate by contract type
plt.figure(figsize=(6,4))
sns.barplot(
    data=df,
    x="Contract",
    y=df["Churn"].apply(lambda x: 1 if x=="Yes" else 0)
)
plt.title("Churn Rate by Contract Type")
plt.savefig("reports/contract_churn.png")
plt.close()

print("Reports generated successfully!")
