import streamlit as st
import pandas as pd
import csv

sample_text = "Some text that will be downloaded ."
st.download_button('Download text', sample_text)

with open("Liki.jpg", "rb") as file:
    btn = st.download_button(
        label="Download Image",
        data=file,
        file_name="Like.jpg",
        mime="image/jpg"

    )


@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


df1 = pd.read_csv('topics.csv')
cvs = convert_df(df1)

st.download_button(
    label="Download data as csv",
    data=csv,
    file_name="address.csv",
    mime="text/csv"
)
