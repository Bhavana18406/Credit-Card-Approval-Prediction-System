
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from imblearn.over_sampling import SMOTE
import xgboost as xgb
from src.utils.preprocessing import create_preprocessing_pipeline


def load_and_prepare_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    train_df = pd.read_csv(os.path.join(base_dir, "data", "train.csv"))
    test_df = pd.read_csv(os.path.join(base_dir, "data", "test.csv"))
    full_data = pd.concat([train_df, test_df], axis=0)
    full_data = full_data.sample(frac=1).reset_index(drop=True)
    return full_data


def split_data(df, test_size=0.2):
    train, test = train_test_split(df, test_size=test_size, random_state=42)
    return train.reset_index(drop=True), test.reset_index(drop=True)


def compare_models(X_train, y_train, X_test, y_test):
    models = {
        "Logistic Regression": LogisticRegression(random_state=42, max_iter=1000),
        "Random Forest": RandomForestClassifier(random_state=42),
        "XGBoost": xgb.XGBClassifier(random_state=42, use_label_encoder=False, eval_metric="logloss")
    }
    results = []
    best_model = None
    best_accuracy = 0
    best_model_name = ""
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        results.append({
            "Model": name,
            "Accuracy": accuracy,
            "Recall": recall,
            "Precision": precision,
            "F1 Score": f1
        })
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model
            best_model_name = name
    results_df = pd.DataFrame(results)
    return results_df, best_model, best_model_name


def main():
    print("Loading data...")
    full_data = load_and_prepare_data()
    train_df, test_df = split_data(full_data)
    print("Preprocessing data...")
    pipeline = create_preprocessing_pipeline()
    processed_train = pipeline.fit_transform(train_df)
    processed_test = pipeline.transform(test_df)
    X_train = processed_train.drop(["ID", "Is high risk"], axis=1)
    y_train = processed_train["Is high risk"]
    X_test = processed_test.drop(["ID", "Is high risk"], axis=1)
    y_test = processed_test["Is high risk"]
    print("Oversampling with SMOTE...")
    smote = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
    print("Comparing models...")
    results_df, best_model, best_model_name = compare_models(X_train_balanced, y_train_balanced, X_test, y_test)
    print("\nModel Comparison Results:")
    print(results_df)
    print(f"\nBest Model: {best_model_name} with Accuracy: {results_df.loc[results_df['Model'] == best_model_name, 'Accuracy'].values[0]:.4f}")
    print("Saving best model and preprocessing pipeline...")
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_dir = os.path.join(base_dir, "src", "models")
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(best_model, os.path.join(model_dir, "best_model.pkl"))
    joblib.dump(pipeline, os.path.join(model_dir, "preprocessing_pipeline.pkl"))
    results_df.to_csv(os.path.join(model_dir, "model_comparison_results.csv"), index=False)
    print("Training complete!")


if __name__ == "__main__":
    main()

