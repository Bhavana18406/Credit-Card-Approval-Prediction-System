# 💳 AI-Powered Credit Card Approval System

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-green)
![XGBoost](https://img.shields.io/badge/XGBoost-Model-orange)

An **intelligent machine learning-driven platform** that transforms the credit card approval process by analyzing applicant profiles and generating automated approval/rejection decisions.

The system evaluates demographic, financial, employment, and ownership information to provide faster and more objective lending decisions with additional insights such as risk scores, credit eligibility classification, feature importance analysis, and downloadable prediction reports.

---

# 🌐 Live Demo

🚀 **Streamlit Application**

👉 https://credit-card-approval-tz8zvzevsfqc8tjvwxky7w.streamlit.app

Hosted on **Streamlit Cloud**.

---

# 🚀 Application Flow

```text
Applicant Details
        │
        ▼
Data Preprocessing Pipeline
        │
        ▼
Machine Learning Models
        │
        ▼
Credit Approval Prediction
        │
        ▼
Risk Score + Eligibility + PDF Report
```

---

# ✨ Features

📊 **Smart Predictions**
Uses three machine learning algorithms:

* Logistic Regression
* Random Forest
* XGBoost

to generate accurate credit approval predictions.

🎯 **Risk Scoring**
Calculates a risk score between **0-100** based on prediction confidence.

🏆 **Eligibility Classification**
Classifies applicants into:

* Low Eligibility
* Medium Eligibility
* High Eligibility

🔍 **Feature Insights**
Displays the top 10 most influential factors affecting prediction results.

📝 **Prediction Tracking**
Maintains local history of all prediction results.

📄 **PDF Reporting**
Generates professional downloadable PDF reports.

📱 **Modern Dashboard**
Interactive Streamlit dashboard with clean UI and animations.

---

# 🛠 Tech Stack

| Category             | Technology               |
| -------------------- | ------------------------ |
| Programming Language | Python 3.10+             |
| Web Framework        | Streamlit                |
| Machine Learning     | Scikit-learn, XGBoost    |
| Data Processing      | Pandas, NumPy            |
| Imbalance Handling   | Imbalanced-learn (SMOTE) |
| Model Serialization  | Joblib                   |
| PDF Generation       | ReportLab                |
| UI Enhancement       | Streamlit-Lottie         |

---

# 📊 Dataset Information

The project uses historical credit card application data containing:

### Personal Information

* Age
* Gender
* Marital Status
* Household Size

### Financial Information

* Annual Income
* Employment Status
* Employment Duration

### Asset Information

* Car Ownership
* Property Ownership

### Contact Information

* Phone Availability
* Work Phone Availability
* Email Availability

### Educational Information

* Education Level

---

# 📁 Project Structure

```text
Credit-card-approval-prediction-classification-main/

├── app.py                         ← Main Streamlit Application
│
├── src/
│   ├── train_models.py            ← Model Training & Comparison Script
│   │
│   ├── models/
│   │   ├── best_model.pkl         ← Trained ML Model
│   │   ├── preprocessing_pipeline.pkl
│   │   └── model_comparison_results.csv
│   │
│   └── utils/
│       └── preprocessing.py       ← Data Processing Utilities
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── docs/
│   └── ER_Diagram.md
│
├── notebooks/                     ← Data Analysis Notebooks
├── history/                       ← Prediction History Storage
├── static/                        ← Static Assets
├── requirements.txt
├── LICENSE
└── README.md
```

---

# 🗃️ Entity Relationship Diagram

The system database design contains entities related to users, applicants, credit history, ML models, and prediction results.

Detailed ER Diagram:

```text
docs/ER_Diagram.md
```

---

# ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/Bhavana18406/credit-card-Approval.git

cd credit-card-Approval
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train Machine Learning Models

```bash
python src/train_models.py
```

### 4. Launch Streamlit Application

```bash
streamlit run app.py
```

Application runs at:

```text
http://localhost:8501
```

---

# 📖 Usage Guide

1. Open the Dashboard to view system overview.
2. Navigate to **Credit Prediction**.
3. Enter applicant details.
4. Generate approval prediction.
5. View risk score and eligibility category.
6. Download PDF prediction report.
7. Check Prediction History for previous results.
8. Explore Model Performance comparison.

---

# 🤖 Machine Learning Workflow

### 1. Data Preprocessing

* Data cleaning
* Missing value handling
* Feature transformation
* Categorical encoding

### 2. Class Imbalance Handling

Applied:

```text
SMOTE (Synthetic Minority Oversampling Technique)
```

to balance training data.

### 3. Model Training

Trained models:

| Model               | Description                                     |
| ------------------- | ----------------------------------------------- |
| Logistic Regression | Baseline classification algorithm               |
| Random Forest       | Ensemble learning using multiple decision trees |
| XGBoost             | Gradient boosting algorithm                     |

### 4. Model Evaluation

Models are compared using:

* Accuracy
* Recall
* Precision
* F1 Score

### 5. Model Selection

The best-performing model is selected and deployed for real-time prediction.

---

# 📈 Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 56.23%   |
| Random Forest       | 97.28%   |
| XGBoost             | 81.86%   |

🏆 **Best Model: Random Forest**

Accuracy: **97.28%**

---

# 📋 Input Features

The application collects:

* Gender
* Age (18-70 years)
* Marital Status
* Family Member Count
* Dwelling Type
* Annual Income
* Employment Status
* Employment Length
* Education Level
* Car Ownership
* Property Ownership
* Work Phone Availability
* Phone Availability
* Email Availability

---

# 🎯 Prediction Output

For every application, the system provides:

✅ Approval / Rejection Status
📈 Confidence Score
⚠️ Risk Score (0-100)
🏦 Credit Eligibility Category
📊 Feature Importance Visualization
📄 Downloadable PDF Report

---

# 🔮 Future Enhancements

* Real-time credit bureau integration
* Advanced hyperparameter optimization
* User authentication with role-based access control
* Cloud database integration
* Scalable cloud deployment
* Additional financial stress analysis
* Batch prediction support

---

# 📄 License

This project is licensed under the terms specified in the LICENSE file.

---

# 🚀 Deployment

Platform:

**Streamlit Cloud**

Live Demo:

https://credit-card-approval-prediction-system-zecemst9xmvv9uygnzl2sq.streamlit.app/

---

Built with ❤️ using:

**Python · Streamlit · Scikit-learn · XGBoost · Pandas · NumPy**
