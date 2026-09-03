import streamlit as st
import pandas as pd
import joblib

model = joblib.load("loan_model.pkl")

st.set_page_config(
    page_title="Business Loan Approval System",
    page_icon="💼",
    layout="centered"
)

st.title("💼 Business Loan Approval Prediction System")
st.write("Enter applicant details to estimate loan approval.")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

applicant_income = st.number_input(
    "Applicant Monthly Income",
    min_value=0.0,
    value=5000.0
)

coapplicant_income = st.number_input(
    "Coapplicant Monthly Income",
    min_value=0.0,
    value=0.0
)

loan_amount = st.number_input(
    "Requested Loan Amount",
    min_value=1.0,
    value=150.0
)