
# AI-Powered Credit Card Approval System

## Project Overview

The AI-Powered Credit Card Approval System is an intelligent machine learning-driven platform that transforms how financial institutions evaluate credit card applications. By analyzing comprehensive applicant profiles, the system delivers automated approval/rejection decisions along with actionable insights including risk assessment scores and credit eligibility categorizations, enabling faster and more objective lending decisions.

## Features

- 📊 **Smart Predictions**: Leverages three robust machine learning algorithms (Logistic Regression, Random Forest, XGBoost) to ensure accurate credit card approval forecasts
- 🎯 **Risk Scoring**: Computes a precise risk score (0-100) for every applicant based on model predictions
- 🏆 **Eligibility Classification**: Groups applicants into Low, Medium, or High credit eligibility tiers for quick assessment
- 🔍 **Feature Insights**: Visualizes the top 10 most impactful factors influencing each prediction
- 📝 **Prediction Tracking**: Maintains a local history of all prediction results for future reference
- 📄 **PDF Reporting**: Generates professional, downloadable PDF reports for each prediction
- 📱 **Modern Dashboard**: Clean, intuitive Streamlit-based interface with smooth animations

## Tech Stack

- **Python 3.10+**: Core programming language
- **Streamlit**: Interactive web application framework for data science projects
- **Scikit-learn**: Comprehensive machine learning library for model development
- **XGBoost**: High-performance gradient boosting algorithm
- **Imbalanced-learn**: Tools to handle class imbalance using SMOTE
- **Pandas & NumPy**: Efficient data manipulation and numerical computing
- **Joblib**: Model serialization for persistent storage
- **ReportLab**: Professional PDF document generation
- **Streamlit-lottie**: Beautiful Lottie animations for UI enhancement

## Dataset Information

The project uses a comprehensive dataset of historical credit card applications that includes diverse features such as:

- Personal demographics (age, gender, marital status)
- Financial details (annual income, employment status, employment duration)
- Asset ownership (car, property)
- Contact information (phone, email)
- Educational background
- Household size

## Project Structure

```
Credit-card-approval-prediction-classification-main/
├── app.py                      # Main Streamlit application
├── src/
│   ├── train_models.py         # Model training and comparison script
│   ├── models/                 # Trained models and preprocessing pipeline
│   └── utils/                  # Preprocessing utility functions
├── data/                       # Training and test datasets
├── docs/                       # Project documentation
├── notebooks/                  # Jupyter notebooks and data profiling
├── static/                     # Static assets and images
├── history/                    # Prediction history storage
├── requirements.txt            # Python dependencies
├── LICENSE                     # Project license
└── README.md                   # This file
```

## Entity Relationship Diagram

For detailed information about the data model and entity relationships, please refer to [ER_Diagram.md](docs/ER_Diagram.md).

## Installation

1. **Clone or download the repository** from GitHub Repository
2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Train the machine learning models** (run once before first use):
   ```bash
   python src/train_models.py
   ```
4. **Launch the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. Visit the **Dashboard** to get an overview of the system
2. Navigate to **Credit Prediction** to enter applicant information and receive predictions
3. Check **Prediction History** to review all previous prediction results
4. Explore **Model Performance** to view comparison metrics between different ML models

## Machine Learning Workflow

1. **Data Preprocessing**: Clean and transform raw data, handle missing values, and encode categorical features
2. **Class Imbalance Handling**: Apply SMOTE to balance the training dataset
3. **Model Training**: Train three different models (Logistic Regression, Random Forest, XGBoost)
4. **Model Evaluation**: Compare models using accuracy, recall, precision, and F1 score
5. **Model Selection**: Choose the best-performing model for production use
6. **Prediction Pipeline**: Deploy the selected model with preprocessing pipeline for real-time predictions

## Models Used

| Model               | Description                                  |
|---------------------|----------------------------------------------|
| Logistic Regression | Simple yet effective baseline classifier     |
| Random Forest       | Ensemble method with multiple decision trees |
| XGBoost             | Gradient boosting with exceptional performance |

## Application Flow

1. User inputs applicant details through the Streamlit interface
2. Input data is processed through the pre-trained pipeline
3. The best model generates a prediction with confidence score
4. Risk score and eligibility tier are calculated
5. Results are displayed with feature importance visualization
6. Prediction is saved to local history
7. PDF report is available for download

## Input Features

The application collects the following applicant information:

- Gender
- Age (18-70 years)
- Marital status
- Family member count
- Dwelling type
- Annual income
- Employment status
- Employment length (years)
- Education level
- Car ownership
- Property ownership
- Work phone availability
- Phone availability
- Email availability

## Prediction Output

For each application, the system provides:

- **Approval Status**: Clear Approved/Rejected decision
- **Confidence Score**: Percentage indicating model certainty
- **Risk Score**: 0-100 score assessing applicant risk
- **Credit Eligibility**: Low/Medium/High eligibility tier
- **Feature Importance**: Visualization of top influencing factors
- **PDF Report**: Comprehensive downloadable report

## Future Enhancements

- Integration with real-time credit bureau data sources
- Advanced hyperparameter optimization for improved accuracy
- User authentication with role-based access control
- Cloud deployment for scalable, accessible service
- Additional financial analysis and stress testing modules
- Batch prediction capabilities for multiple applications


## License

This project is licensed under the terms specified in the LICENSE file.

## Live Demo

Live Demo: https://credit-card-approval-tz8zvzevsfqc8tjvwxky7w.streamlit.app

## Screenshots

[Placeholder for screenshots]

