import streamlit as st
import pandas as pd
import pickle

st.title("Healthcare Cost Prediction App")

df = pd.read_csv("insurance.csv")
model = pickle.load(open("healthcare_model.pkl", "rb"))

age = st.sidebar.number_input("Enter Age", min_value=18, max_value=100, value=25)

sex = st.sidebar.selectbox("Select Gender", sorted(df["sex"].unique()))

bmi = st.sidebar.number_input("Enter BMI", min_value=10.0, max_value=60.0, value=25.0)

children = st.sidebar.number_input("Number of Children", min_value=0, max_value=10, value=0)

smoker = st.sidebar.selectbox("Smoking Status", sorted(df["smoker"].unique()))

region = st.sidebar.selectbox("Select Region", sorted(df["region"].unique()))

if st.sidebar.button("Predict Charges"):

    st.write("### Patient Details")
    st.write("Age :", age)
    st.write("Gender :", sex)
    st.write("BMI :", bmi)
    st.write("Children :", children)
    st.write("Smoker :", smoker)
    st.write("Region :", region)

    columns = ["age", "sex", "bmi", "children", "smoker", "region"]

    myinput = [[age, sex, bmi, children, smoker, region]]

    myinput = pd.DataFrame(myinput, columns=columns)

    result = model.predict(myinput)

    st.success("Estimated Medical Charges : ₹ {:.2f}".format(result[0]))