import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def get_session_df():
    if st.session_state.get("df") is None:
        st.error("Upload data first")
        st.stop()
    else:
        return st.session_state.df


def get_model_hyper_params(df):
    df["params"] = df["params"].apply(lambda x: eval(x))

    return df["params"].iloc[0].keys()


def get_param_view_selector(model_hyper_params):
    return st.sidebar.selectbox(
        "Select a parameter to view",
        model_hyper_params,
        help="Select which parameter to view all values for",
    )


def get_sliders(df, model_hyper_params, param_to_view):
    return {
        param: st.sidebar.select_slider(
            param,
            options=df[f"param_{param}"].unique(),
            disabled=True if param_to_view == param else False,
            on_change=None if param_to_view == param else None,
        )
        for param in model_hyper_params
    }


def get_df_query(sliders, param_to_view):
    return " & ".join(
        [
            f"param_{param} == {sliders[param]}"
            for param in sliders
            if param != param_to_view
        ]
    )


def filter_df(df, query):
    return df.query(query)


def plot_results(df, param_to_view):
    fig = px.line(
        df,
        x=f"param_{param_to_view}",
        y=["mean_test_score", "mean_train_score"],
        title=f"Mean Test and Train Scores for {param_to_view}",
    )
    return fig


def model_eval():
    df = get_session_df()
    model_hyper_params = get_model_hyper_params(df)
    param_to_view = get_param_view_selector(model_hyper_params)
    sliders = get_sliders(df, model_hyper_params, param_to_view)
    query = get_df_query(sliders, param_to_view)
    df = filter_df(df, query)
    fig = plot_results(df, param_to_view)
    st.plotly_chart(fig)
