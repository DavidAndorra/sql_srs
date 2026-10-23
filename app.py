import streamlit as st
import pandas as pd
import duckdb

#st.header("SQL SRS")
st.write("""
         # SQL SRS Pierre
         Spaced Repetition System SQL practice
         """)

option = st.selectbox(
    "What would you like to review?",
    ("Joins","Group by","Windows Functions"),
    index=None,
    placeholder="Select a theme ...",
)

st.write("""
         # Deuxieme partie
         Spaced Repetition System SQL practice
         """)


option = st.selectbox(
    "What would you like to review the next time?",
    ("Joins","Group by","Windows Functions"),
    index=None,
    placeholder="Select a theme ...",
)