import streamlit as st
from routes import start, upload, model_eval


def main():
    pages = {
        "Start": start,
        "Upload": upload,
        "Model Evaluation": model_eval,
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page()


if __name__ == "__main__":
    main()
