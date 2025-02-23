# Imports

import streamlit as st
import pandas as pd
import os
from io import BytesIO


# Set up Our App

st.set_page_config(page_title="Kashif Ali App", layout="wide")
st.title("Kashif Ali")
st.write(
    "Transfrom your files between CSV and Excel formats with built-in data cleaning and visualization!"
)

uploaded_files = st.file_uploader(
    "Upload you files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_excel(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"unsupported file type: {file_ext}")
            continue

        # Display info about the file

        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024}")

        # Show 5 rows of Our df
        st.write("Preview the Head of the Data Fram")
        st.dataframe(df.head())

        
