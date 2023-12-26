import streamlit as st
import pandas as pd


class WrongFileType(Exception):
    pass


class WrongFileContents(Exception):
    pass


def _exception_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            st.error(e)
            st.stop()

    return wrapper


@_exception_wrapper
def _evaluate_file_type(uploaded_file):
    if uploaded_file.type != "text/csv":
        raise WrongFileType("File type is not 'text/csv' | Did you upload a csv file?")


@_exception_wrapper
def _evaluate_file_contents(df):
    param_cols = [col for col in df.columns if col.startswith("param_")]
    if not param_cols:
        raise WrongFileContents(
            "No columns with name 'param_*' found | Did you upload a cv_results_.csv file?"
        )
    if "mean_test_score" not in df.columns:
        raise WrongFileContents(
            "No column with name 'mean_test_score' found | Did you upload a cv_results_.csv file?"
        )
    if "mean_train_score" not in df.columns:
        raise WrongFileContents(
            "No column with name 'mean_train_score' found | Did you upload a cv_results_.csv file?"
        )


def upload_file():
    uploaded_file = st.file_uploader("Upload a 'cv_results_' file")

    if uploaded_file is not None:
        st.success("File uploaded successfully!")

        _evaluate_file_type(uploaded_file)

        dataframe = pd.read_csv(uploaded_file, index_col=0)

        with st.spinner("Evaluating file contents..."):
            _evaluate_file_contents(dataframe)
            st.success("File contents evaluated successfully!")
            st.session_state.df = dataframe
            st.session_state.filename = uploaded_file.name
            st.write(dataframe)
