import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open('../models/churn_pipeline.pkl', 'rb'))

st.set_page_config(page_title="Churn Prediction", layout="centered")

st.title("📊 Customer Churn Prediction App")

st.write("Predict whether a customer is likely to churn")

# Input fields
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check",
    "Bank transfer (automatic)", "Credit card (automatic)"
])

internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

senior = st.selectbox("Senior Citizen", [0, 1])

# Convert input into dataframe
input_data = pd.DataFrame({
    'tenure': [tenure],
    'MonthlyCharges': [monthly_charges],
    'Contract': [contract],
    'PaymentMethod': [payment_method],
    'InternetService': [internet_service],
    'SeniorCitizen': [senior]
})

# Prediction
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Churn ({probability:.2f})")
    else:
        st.success(f"✅ Low Risk of Churn ({probability:.2f})")  