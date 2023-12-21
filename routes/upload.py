import streamlit as st
import pandas as pd


def upload():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            session = st.session_state
            session.df = df
            st.write(df)
        except Exception as e:
            print(e)
            st.write(f"Error uploading file: {e}")
