# 💰 Financial Risk Analytics for Loan Approval

## 📌 Project Overview

Financial institutions receive thousands of loan applications every day. Approving loans without proper risk assessment can lead to financial losses due to loan defaults. This project leverages Machine Learning to analyze applicant information and predict whether a loan application should be approved based on financial risk.

The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and prediction to assist financial institutions in making data-driven lending decisions.

---

# 🎯 Problem Statement

The objective of this project is to build a Machine Learning model that predicts loan approval by analyzing applicant financial and demographic information.

The model helps financial institutions:

- Reduce the risk of loan defaults.
- Automate loan approval decisions.
- Improve credit risk assessment.
- Increase decision-making efficiency.
- Support data-driven lending strategies.

---

# 📊 Dataset

The dataset contains applicant financial and personal information.

### Features

| Feature | Description |
|---------|-------------|
| Applicant Income | Monthly income of the applicant |
| Coapplicant Income | Monthly income of the co-applicant |
| Loan Amount | Requested loan amount |
| Loan Amount Term | Loan repayment period |
| Credit History | Previous credit repayment history |
| Education | Graduate / Not Graduate |
| Employment Status | Self-employed or not |
| Marital Status | Married / Unmarried |
| Gender | Applicant gender |
| Property Area | Urban, Semi-Urban, Rural |
| Dependents | Number of dependents |
| Loan Status | Target Variable |

---

# 🎯 Target Variable

| Value | Meaning |
|--------|----------|
| Y | Loan Approved |
| N | Loan Rejected |

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

# 📚 Libraries Used

```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

import joblib
```

---

# 📂 Project Structure

```
Financial-Risk-Analytics-for-Loan-Approval/
│
├── data/
│      └── loan_data.csv
│
├── notebooks/
│      └── Loan_Approval_Analysis.ipynb
│
├── models/
│      └── loan_approval_model.pkl
│
├── src/
│      ├── preprocessing.py
│      ├── train.py
│      ├── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

---

# 🔍 Exploratory Data Analysis (EDA)

Performed analyses include:

- Dataset Overview
- Missing Value Analysis
- Duplicate Detection
- Data Type Inspection
- Statistical Summary
- Target Class Distribution
- Income Distribution
- Loan Amount Distribution
- Credit History Analysis
- Correlation Heatmap
- Feature Relationships
- Outlier Detection

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Missing value imputation
- Duplicate removal
- Categorical encoding
- Feature scaling
- Feature selection
- Train-Test split

---

# ⚙️ Feature Engineering

The preprocessing pipeline includes:

- **SimpleImputer** for handling missing values.
- **OneHotEncoder** for categorical features.
- **StandardScaler** for numerical features.
- **ColumnTransformer** to process different feature types.
- **Pipeline** for reproducible preprocessing and model training.

---

# 🤖 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

The best-performing model was selected based on evaluation metrics.

---

# 📈 Model Evaluation

Classification metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix
- Classification Report

---

# 🔄 Project Workflow

```
Loan Dataset
      │
      ▼
Data Cleaning
      │
      ▼
EDA
      │
      ▼
Feature Engineering
      │
      ▼
Encoding & Scaling
      │
      ▼
Train-Test Split
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Best Model Selection
      │
      ▼
Model Saving
      │
      ▼
Loan Approval Prediction
```

---

# 💾 Model Saving

The trained model is saved using Joblib.

```python
joblib.dump(model, "loan_approval_model.pkl")
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Financial-Risk-Analytics-for-Loan-Approval.git
```

Navigate to the project directory:

```bash
cd Financial-Risk-Analytics-for-Loan-Approval
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

# 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
```

---

# 📊 Example Prediction

### Input

```
Applicant Income : 6500
Coapplicant Income : 2500
Loan Amount : 180
Credit History : 1
Education : Graduate
Employment : No
Property Area : Urban
```

### Output

```
Loan Status : Approved ✅
Approval Probability : 96%
```

---

# 📊 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Missing Value Imputation
- Feature Scaling
- One-Hot Encoding
- Pipeline
- ColumnTransformer
- Classification Models
- Model Evaluation
- Financial Risk Analytics
- Python Programming
- Data Visualization

---

# 💼 Business Value

This project enables financial institutions to:

- Improve loan approval accuracy.
- Reduce default risk.
- Automate credit risk assessment.
- Enhance operational efficiency.
- Support consistent and unbiased lending decisions.

---

# 🔮 Future Improvements

- Hyperparameter Tuning
- XGBoost Classifier
- LightGBM Classifier
- CatBoost Classifier
- Cross Validation
- SHAP Explainability
- Streamlit Dashboard
- FastAPI REST API
- Docker Containerization
- Cloud Deployment (AWS/Azure/GCP)
- MLOps Integration
- Real-time Loan Scoring

---

# 📖 Learning Outcomes

Through this project, I learned:

- Building end-to-end classification pipelines.
- Handling mixed numerical and categorical data.
- Using preprocessing pipelines for production-ready ML.
- Comparing multiple classification algorithms.
- Evaluating models with appropriate classification metrics.
- Applying machine learning to real-world financial risk problems.

---

# 👨‍💻 Author

**Mahesh Gurme**

### Skills

- Data Science
- Machine Learning
- Financial Analytics
- Python
- SQL
- Power BI
- Deep Learning
- Artificial Intelligence

---

# ⭐ If you found this project useful, consider giving it a star on GitHub!
