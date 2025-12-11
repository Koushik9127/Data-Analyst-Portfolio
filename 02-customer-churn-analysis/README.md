# 📊 Customer Churn Analysis

This project analyzes telecom customer churn using a fully terminal-driven workflow.  
All KPIs, charts, and machine-learning results are generated using a single script and stored inside the `reports/` folder.

---

## 📁 Project Structure

02-customer-churn-analysis/
│── data/
│ └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│── scripts/
│ └── generate_results.py
│── reports/
│ ├── kpis.txt
│ ├── churn_distribution.png
│ ├── correlation_heatmap.png
│ ├── feature_importance.png
│ └── model_metrics.png
└── README.md

---

## 🎯 Objective
Identify key factors influencing customer churn and build models to predict churn probability.

---

## 🔧 Automated Workflow (via Terminal)

The script performs the entire pipeline:

### **1. Data Cleaning**
- Convert `TotalCharges` to numeric  
- Handle missing values  
- Encode categorical variables  
- Convert churn to binary (Yes/No → 1/0)  

### **2. Exploratory Data Analysis**
Generates:
- Churn distribution plot  
- Correlation heatmap  
- Summary KPIs  

### **3. Machine Learning Models**
Trains 3 ML models:
- Logistic Regression  
- Random Forest  
- XGBoost  

Metrics calculated:
- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  

### **4. Reporting**
Outputs saved automatically to `reports/`:
- `kpis.txt`
- `churn_distribution.png`
- `correlation_heatmap.png`
- `feature_importance.png`
- `model_metrics.png`

---

## ▶️ How to Run (Terminal)

### **1. Go to project folder**
cd ~/data-analyst-portfolio/02-customer-churn-analysis

### **2. Run entire workflow**
python scripts/generate_results.py

### **3. Check generated results**
ls reports/

---

## 📦 Output Files Overview

| File | Description |
|------|-------------|
| kpis.txt | Model evaluation metrics |
| churn_distribution.png | Visual churn rate |
| correlation_heatmap.png | Feature correlation matrix |
| feature_importance.png | Important drivers of churn |
| model_metrics.png | Side-by-side model comparison |

---

## 🧠 Key Insights
- High monthly charges and low tenure strongly drive churn  
- Contract type and payment method significantly impact churn  
- Random Forest/XGBoost provide the best prediction accuracy  

---

## 🛠 Tech Stack
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-Learn  
- XGBoost  
- Terminal (zsh)

