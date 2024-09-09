import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Loan Eligibility Prediction")


# Function to predict loan eligibility
def predict_eligibility(married, dependents, applicant_income, coapplicant_income, loan_amount, loan_amount_term,
                        credit_history, property_area):
    # Create an array for prediction
    input_data = np.array([[married, dependents, applicant_income, coapplicant_income, loan_amount, loan_amount_term,
                            credit_history, property_area]])

    # Make prediction
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        return "Eligible"
    else:
        return "Not Eligible"


# Input fields in Streamlit
married = st.selectbox("Married", [0, 1])  # 0: No, 1: Yes
dependents = st.selectbox("Dependents", [0, 1, 2, 3])  # Number of dependents
applicant_income = st.number_input("Applicant Income", min_value=0.0, step=100.0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, step=100.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0, step=100.0)
loan_amount_term = st.selectbox("Loan Amount Term (in days)", [360, 120, 240, 180, 60, 300, 480, 36, 84, 12, 350, 6])
credit_history = st.selectbox("Credit History", [0, 1])  # 0 for bad, 1 for good
property_area = st.selectbox("Property Area", [0, 1, 2])  # Assuming encoded values for areas

# Button to predict
if st.button("Predict Loan Eligibility"):
    result = predict_eligibility(married, dependents, applicant_income, coapplicant_income, loan_amount,
                                 loan_amount_term, credit_history, property_area)
    st.success(f"The applicant is {result} for the loan.")

# Footer
st.write("Developed with Streamlit")
