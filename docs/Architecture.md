
# System Architecture

## Overview

The AI-Powered Credit Card Approval System is built using a modular, maintainable architecture that separates concerns across different components.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        User Interface                            │
│                      (Streamlit Dashboard)                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Application Logic Layer                      │
│  - Input Handling  - Prediction Orchestration  - Report Generation│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Machine Learning Layer                        │
│  - Preprocessing Pipeline  - Model Inference  - Model Training  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Data Storage Layer                        │
│  - Dataset Files  - Model Persistence  - Prediction History     │
└─────────────────────────────────────────────────────────────────┘
```

## Component Descriptions

### 1. User Interface Layer (app.py)
- **Technology**: Streamlit
- **Responsibilities**:
  - Display interactive dashboard
  - Collect applicant input data
  - Show prediction results and visualizations
  - Provide navigation between different sections

### 2. Application Logic Layer
- **Responsibilities**:
  - Validate user inputs
  - Coordinate preprocessing and prediction steps
  - Calculate risk scores and eligibility levels
  - Generate PDF reports
  - Manage prediction history

### 3. Machine Learning Layer
- **Preprocessing Pipeline** (src/utils/preprocessing.py):
  - Outlier removal
  - Feature engineering
  - Encoding categorical variables
  - Feature scaling
- **Model Training** (src/train_models.py):
  - Train multiple ML algorithms
  - Compare model performance
  - Save best model and pipeline

### 4. Data Storage Layer
- **data/**: Raw and processed datasets
- **src/models/**: Trained model files and preprocessing pipeline
- **history/**: Saved prediction history in JSON format
- **static/**: Static assets

## Data Flow

1. User enters applicant information through the UI
2. Input data is validated
3. Data is passed through the preprocessing pipeline
4. Processed data is fed into the trained ML model
5. Model generates prediction and confidence score
6. Risk score and eligibility level are calculated
7. Results are displayed to the user
8. Prediction is saved to history
