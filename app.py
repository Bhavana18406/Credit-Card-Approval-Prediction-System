
import os
import json
import numpy as np
import pandas as pd
import joblib
import streamlit as st
from streamlit_lottie import st_lottie
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import io

st.set_page_config(page_title="AI-Powered Credit Card Approval System", page_icon="💳", layout="wide")


def load_lottie_file(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottie_url(url):
    """
    Safely load a Lottie animation from a URL.
    Handles all connection and request errors gracefully.
    Returns: Lottie JSON if successful, None otherwise
    """
    try:
        import requests
        r = requests.get(url, timeout=10)  # Add timeout to prevent hanging
        if r.status_code == 200:
            return r.json()
        return None
    except Exception:
        # Catch any error (connection errors, timeouts, invalid JSON, etc.)
        return None


def safe_load_prediction_history():
    """
    Safely load prediction history from JSON file.
    Handles:
    - File not found: creates new empty file
    - Empty file: initializes with []
    - Invalid/corrupted JSON: recreates with []
    Returns: list of prediction history entries
    """
    history_file = "history/prediction_history.json"
    os.makedirs("history", exist_ok=True)
    history = []
    try:
        if os.path.exists(history_file):
            with open(history_file, "r", encoding="utf-8") as f:
                # Try to load JSON
                loaded = json.load(f)
                # Verify it's a list
                if isinstance(loaded, list):
                    history = loaded
                else:
                    # If not a list, reset to empty
                    history = []
    except json.JSONDecodeError:
        # Invalid JSON, reset to empty
        history = []
    except Exception as e:
        # Any other error, reset to empty
        history = []
    
    # If history is empty (either new file or reset), save empty array
    if not history:
        try:
            with open(history_file, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)
        except Exception as e:
            # Just in case saving fails, we still have empty history in memory
            pass
    
    return history


def save_prediction_history(history):
    """
    Save prediction history to JSON file with indent=4.
    Creates directory if needed.
    """
    history_file = "history/prediction_history.json"
    os.makedirs("history", exist_ok=True)
    try:
        with open(history_file, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4)
    except Exception as e:
        # If save fails, we can log but don't crash app
        pass


def init_session_state():
    if "prediction_history" not in st.session_state:
        # Load history from file on app start
        st.session_state.prediction_history = safe_load_prediction_history()
    if "model" not in st.session_state:
        if os.path.exists("src/models/best_model.pkl") and os.path.exists("src/models/preprocessing_pipeline.pkl"):
            st.session_state.model = joblib.load("src/models/best_model.pkl")
            st.session_state.pipeline = joblib.load("src/models/preprocessing_pipeline.pkl")
        else:
            st.session_state.model = None
            st.session_state.pipeline = None


def calculate_risk_score(prediction_probability):
    risk_score = (1 - prediction_probability) * 100
    return round(risk_score, 2)


def get_credit_eligibility(risk_score):
    if risk_score >= 75:
        return "High", colors.green
    elif risk_score >= 50:
        return "Medium", colors.orange
    else:
        return "Low", colors.red


def create_prediction_pdf(prediction_data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    story.append(Paragraph("AI-Powered Credit Card Approval System - Prediction Report", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles["Normal"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Applicant Details:", styles["Heading2"]))
    data = []
    for key, value in prediction_data["input_data"].items():
        data.append([key, str(value)])
    table = Table(data)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(table)
    story.append(Spacer(1, 12))
    story.append(Paragraph("Prediction Results:", styles["Heading2"]))
    story.append(Paragraph(f"Approval Status: {'Approved' if prediction_data['approved'] else 'Rejected'}", styles["Normal"]))
    story.append(Paragraph(f"Prediction Confidence: {prediction_data['confidence']}%", styles["Normal"]))
    story.append(Paragraph(f"Risk Score: {prediction_data['risk_score']}/100", styles["Normal"]))
    story.append(Paragraph(f"Credit Eligibility: {prediction_data['eligibility']}", styles["Normal"]))
    doc.build(story)
    buffer.seek(0)
    return buffer


def main():
    init_session_state()
    lottie_credit = load_lottie_url("https://assets3.lottiefiles.com/packages/lf20_5njp3vgg.json")
    menu = st.sidebar.selectbox("Navigation", ["🏠 Dashboard", "🔍 Credit Prediction", "📊 Prediction History", "📈 Model Performance"])
    if menu == "🏠 Dashboard":
        st.title("🏠 AI-Powered Credit Card Approval System Dashboard")
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if lottie_credit:
                st_lottie(lottie_credit, height=300, key="credit")
            else:
                # Fallback if Lottie fails to load
                st.markdown("""
                <div style="text-align: center; padding: 40px 0;">
                    <div style="font-size: 80px;">💳</div>
                </div>
                """, unsafe_allow_html=True)
        with col2:
            st.markdown("### Welcome!")
            st.write("This system uses advanced machine learning models to predict credit card approvals based on applicant information.")
            st.markdown("### Key Features:")
            st.markdown("✅ Accurate prediction using multiple ML models")
            st.markdown("✅ Risk score and credit eligibility assessment")
            st.markdown("✅ Feature importance visualization")
            st.markdown("✅ Prediction history tracking")
            st.markdown("✅ PDF report generation")
        with col3:
            st.markdown("### Quick Stats")
            total_predictions = len(st.session_state.prediction_history)
            approved = len([p for p in st.session_state.prediction_history if p["approved"]])
            rejected = total_predictions - approved
            st.metric("Total Predictions", total_predictions)
            st.metric("Approved", approved)
            st.metric("Rejected", rejected)
    elif menu == "🔍 Credit Prediction":
        st.title("🔍 Credit Card Approval Prediction")
        st.markdown("---")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("Applicant Information")
            input_gender = st.selectbox("Gender", ["Male", "Female"])
            input_age = st.slider("Age", min_value=18, max_value=70, value=30)
            input_marital_status = st.selectbox("Marital Status", ["Married", "Single/not married", "Civil marriage", "Separated", "Widowed"])
            input_family_size = st.number_input("Family Member Count", min_value=1, max_value=10, value=2)
            input_dwelling = st.selectbox("Dwelling Type", ["House / apartment", "Live with parents", "Municipal apartment ", "Rented apartment", "Office apartment", "Co-op apartment"])
            input_income = st.number_input("Annual Income (USD)", min_value=0, value=50000)
            input_employment_status = st.selectbox("Employment Status", ["Working", "Commercial associate", "Pensioner", "State servant", "Student"])
            input_employment_length = st.slider("Employment Length (Years)", min_value=0, max_value=40, value=5)
            input_education = st.selectbox("Education Level", ["Secondary school", "Higher education", "Incomplete higher", "Lower secondary", "Academic degree"])
        with col2:
            st.subheader("Additional Information")
            input_car = st.selectbox("Owns a Car?", ["Yes", "No"])
            input_property = st.selectbox("Owns Property?", ["Yes", "No"])
            input_work_phone = st.selectbox("Has Work Phone?", ["Yes", "No"])
            input_phone = st.selectbox("Has Phone?", ["Yes", "No"])
            input_email = st.selectbox("Has Email?", ["Yes", "No"])
        marital_map = {
            "Married": "Married",
            "Single/not married": "Single / not married",
            "Civil marriage": "Civil marriage",
            "Separated": "Separated",
            "Widowed": "Widow"
        }
        dwelling_map = {
            "House / apartment": "House / apartment",
            "Live with parents": "With parents",
            "Municipal apartment ": "Municipal apartment",
            "Rented apartment": "Rented apartment",
            "Office apartment": "Office apartment",
            "Co-op apartment": "Co-op apartment"
        }
        employment_map = {
            "Working": "Working",
            "Commercial associate": "Commercial associate",
            "Pensioner": "Pensioner",
            "State servant": "State servant",
            "Student": "Student"
        }
        education_map = {
            "Secondary school": "Secondary / secondary special",
            "Higher education": "Higher education",
            "Incomplete higher": "Incomplete higher",
            "Lower secondary": "Lower secondary",
            "Academic degree": "Academic degree"
        }
        predict_btn = st.button("Predict Credit Approval", type="primary")
        if predict_btn:
            if st.session_state.model is None or st.session_state.pipeline is None:
                st.error("Model not found! Please run the training script first.")
            else:
                with st.spinner("Processing prediction..."):
                    profile_data = [
                        0,
                        input_gender[0],
                        input_car[0],
                        input_property[0],
                        0,
                        input_income,
                        employment_map[input_employment_status],
                        education_map[input_education],
                        marital_map[input_marital_status],
                        dwelling_map[input_dwelling],
                        -input_age * 365.25,
                        -input_employment_length * 365.25,
                        1,
                        1 if input_work_phone == "Yes" else 0,
                        1 if input_phone == "Yes" else 0,
                        1 if input_email == "Yes" else 0,
                        "Placeholder",
                        input_family_size,
                        0.0,
                        0
                    ]
                    train_df = pd.read_csv("data/train.csv")
                    profile_df = pd.DataFrame([profile_data], columns=train_df.columns)
                    combined_df = pd.concat([train_df, profile_df], ignore_index=True)
                    processed = st.session_state.pipeline.fit_transform(combined_df)
                    processed_profile = processed[processed["ID"] == 0].drop(["ID", "Is high risk"], axis=1)
                    prediction = st.session_state.model.predict(processed_profile)[0]
                    prediction_prob = st.session_state.model.predict_proba(processed_profile)[0]
                    approved = prediction == 0
                    confidence = round(prediction_prob[0] * 100 if approved else prediction_prob[1] * 100, 2)
                    risk_score = calculate_risk_score(prediction_prob[0])
                    eligibility, _ = get_credit_eligibility(risk_score)
                    input_dict = {
                        "Gender": input_gender,
                        "Age": input_age,
                        "Marital Status": input_marital_status,
                        "Family Size": input_family_size,
                        "Dwelling Type": input_dwelling,
                        "Annual Income": f"${input_income:,}",
                        "Employment Status": input_employment_status,
                        "Employment Length": f"{input_employment_length} years",
                        "Education Level": input_education,
                        "Owns Car": input_car,
                        "Owns Property": input_property,
                        "Has Work Phone": input_work_phone,
                        "Has Phone": input_phone,
                        "Has Email": input_email
                    }
                    prediction_result = {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "input_data": input_dict,
                        "approved": approved,
                        "confidence": confidence,
                        "risk_score": risk_score,
                        "eligibility": eligibility
                    }
                    st.session_state.prediction_history.append(prediction_result)
                    # Save history using our helper function
                    save_prediction_history(st.session_state.prediction_history)
                st.markdown("---")
                res_col1, res_col2 = st.columns(2)
                with res_col1:
                    if approved:
                        st.success("🎉 APPROVED!")
                        st.balloons()
                    else:
                        st.error("❌ REJECTED")
                    st.metric("Prediction Confidence", f"{confidence}%")
                    st.metric("Risk Score", f"{risk_score}/100")
                    st.metric("Credit Eligibility", eligibility)
                with res_col2:
                    try:
                        if hasattr(st.session_state.model, 'feature_importances_'):
                            importances = st.session_state.model.feature_importances_
                            feature_names = processed_profile.columns
                            importance_df = pd.DataFrame({
                                "Feature": feature_names,
                                "Importance": importances
                            }).sort_values(by="Importance", ascending=False).head(10)
                            st.subheader("Top 10 Feature Importances")
                            st.bar_chart(importance_df.set_index("Feature"))
                    except Exception as e:
                        st.info("Feature importance not available for this model.")
                pdf_buffer = create_prediction_pdf(prediction_result)
                st.download_button(
                    label="📄 Download Prediction Report",
                    data=pdf_buffer,
                    file_name=f"credit_prediction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                    mime="application/pdf"
                )
    elif menu == "📊 Prediction History":
        st.title("📊 Prediction History")
        st.markdown("---")
        # History is already loaded in session state on app start
        if len(st.session_state.prediction_history) > 0:
            history_df = pd.DataFrame(st.session_state.prediction_history)
            history_df["Status"] = history_df["approved"].apply(lambda x: "✅ Approved" if x else "❌ Rejected")
            st.dataframe(history_df[["timestamp", "Status", "confidence", "risk_score", "eligibility"]], use_container_width=True)
        else:
            st.info("No predictions yet. Make a prediction first!")
    elif menu == "📈 Model Performance":
        st.title("📈 Model Performance")
        st.markdown("---")
        results_file = "src/models/model_comparison_results.csv"
        if os.path.exists(results_file):
            results_df = pd.read_csv(results_file)
            st.subheader("Model Comparison Results")
            st.dataframe(results_df, use_container_width=True)
            st.bar_chart(results_df.set_index("Model")[["Accuracy", "Recall", "Precision", "F1 Score"]])
        else:
            st.info("Model comparison results not available. Please run the training script first.")


if __name__ == "__main__":
    main()

