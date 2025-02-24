# Imports
import streamlit as st
import pandas as pd
import os
from io import BytesIO
import importlib.util

# Check if openpyxl is installed
if not importlib.util.find_spec("openpyxl"):
    st.error("The 'openpyxl' library is required to read Excel files. Please install it using `pip install openpyxl`.")
    st.stop()

# Set up Our App
st.set_page_config(page_title="Kashif Ali App", layout="wide")
st.title("💽 Kashif Ali App")
st.write(
    "Transform your files between CSV and Excel formats with built-in data cleaning and visualization!"
)

uploaded_files = st.file_uploader(
    "Upload your files (CSV or Excel):",
    type=["csv", "xlsx"],
    accept_multiple_files=True,
)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read the file based on its extension
        try:
            if file_ext == ".csv":
                df = pd.read_csv(file)  # Use read_csv for CSV files
            elif file_ext == ".xlsx":
                df = pd.read_excel(
                    file, engine="openpyxl"
                )  # Use read_excel for Excel files
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue
        except Exception as e:
            st.error(f"Error reading file {file.name}: {e}")
            continue

        # Display info about the file
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")  # Format file size in KB

        # Show 5 rows of the DataFrame
        st.write("Preview the Head of the DataFrame:")
        st.dataframe(df.head())

        # Option for data cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values Have Been Filled!")

        # Choose Specific Columns to Keep or Convert
        st.subheader("Select Columns to Convert")
        columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Create Some Visualizations
        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            # Check if the DataFrame has a date/time column
            date_col = None
            for col in df.columns:
                if pd.api.types.is_datetime64_any_dtype(df[col]):
                    date_col = col
                    break

            if date_col:
                st.write(f"Time-series data found. Using column '{date_col}' as the x-axis.")
                numeric_cols = df.select_dtypes(include="number").columns
                if len(numeric_cols) == 0:
                    st.warning("No numeric columns found for visualization.")
                else:
                    # Let the user choose which numeric column to plot
                    selected_column = st.selectbox(
                        f"Select a numeric column to plot for {file.name}",
                        numeric_cols
                    )
                    # Plot the selected column over time
                    st.line_chart(df.set_index(date_col)[selected_column])
            else:
                st.warning("No date/time column found. Using default numeric columns for visualization.")
                numeric_cols = df.select_dtypes(include="number").columns
                if len(numeric_cols) == 0:
                    st.warning("No numeric columns found for visualization.")
                elif len(numeric_cols) == 1:
                    st.write(f"Plotting the only numeric column: {numeric_cols[0]}")
                    st.bar_chart(df[numeric_cols[0]])
                else:
                    st.write("Plotting the first two numeric columns:")
                    st.bar_chart(df[numeric_cols[:2]])

        # Convert the File -> CSV to Excel
        st.subheader("Conversion Option")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("🎉 All Files Processed!")