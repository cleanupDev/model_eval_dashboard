import streamlit as st


def start():
    st.title("Welcome to the ML Model Evaluation App")
    st.write(
        "This app is designed to help you evaluate your ML model based on the cv_results_ of your model"
    )
    st.write("Please upload your data to get started")
    st.write("You can upload your data on the left hand side")
    st.write(
        "Once you have uploaded your data, you can go to the Model Evaluation page to view the results"
    )
