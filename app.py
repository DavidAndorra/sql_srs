import streamlit as st
import pandas as pd
import duckdb

#st.header("SQL SRS")
st.write("""
         # SQL SRS
         Spaced Repetition System SQL practice
         """)

option = st.selectbox(
    "What would you like to review?",
    ("Joins","Group by","Windows Functions"),
    index=None,
    placeholder="Select a theme ...",
)

st.write('You selected ',option)

st.write("Original dataframe : df")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)
st.dataframe(df)

tab1, tab2, tab3 = st.tabs(["Cat","Dog","Owl"])


with tab1:
    input_text = st.text_area(label="Enter SQL code")
    st.write("Vous avez entré la query suivante", input_text)
    st.write("New dataframe")
    new_df = duckdb.sql(input_text)
    st.dataframe(new_df)

with tab2 :
    st.header("tab2")

with tab2 :
    st.header("tab3")