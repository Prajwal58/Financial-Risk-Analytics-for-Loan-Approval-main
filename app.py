import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load trained pipeline
# -----------------------------
scaler=joblib.load("scaler.joblib")
model=joblib.load("model.joblib")

st.set_page_config(page_title="Loan Prediction App", layout="centered")

st.title("🏦 Loan Prediction System")
st.write("Predict whether loan will be approved")

# -----------------------------
# User Inputs
# -----------------------------
st.header("Enter Customer Details")

age = st.number_input("Age", min_value=18, max_value=100)

job = st.selectbox("Job", [
    "admin.", "technician", "services", "management",
    "retired", "entrepreneur", "self-employed",
    "blue-collar", "housemaid", "student", "unemployed"
])

marital = st.selectbox("Marital Status", ["single", "married", "divorced"])

education = st.selectbox("Education", ["primary", "secondary", "tertiary"])

default = st.selectbox("Credit Default", ["yes", "no"])
housing = st.selectbox("Housing Loan", ["yes", "no"])
loan = st.selectbox("Personal Loan", ["yes", "no"])

balance = st.number_input("Account Balance", step=100)

# -----------------------------
# Input DataFrame
# -----------------------------
input_df = pd.DataFrame({
    "age": [age],
    "job": [job],
    "marital": [marital],
    "education": [education],
    "default": [default],
    "balance": [balance],
    "housing": [housing],
    "loan": [loan]
})

st.subheader("Input Data")
st.dataframe(input_df)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Loan Status"):
    try:
        prediction = model.predict(input_df)
        result = "Approved ✅" if prediction[0] == 1 else "Rejected ❌"

        st.success(f"Loan Status: **{result}**")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
