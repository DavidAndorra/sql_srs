import streamlit as st
import pandas as pd
import duckdb

st.write("Hello World")

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat","Dog","Owl"])

with tab1:
    st.write("Original dataframe : df")
    st.dataframe(df)
    input_text = st.text_area(label="Enter SQL code")
    st.write("New dataframe")
    new_df = duckdb.sql(input_text)
    st.dataframe(new_df)

with tab2 :
    st.header("tab2")

with tab2 :
    st.header("tab3")