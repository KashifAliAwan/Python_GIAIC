# Imports
import streamlit as st
import pandas as pd
from io import BytesIO

# Check if openpyxl is installed
try:
    import openpyxl
except ImportError:
    st.error("The 'openpyxl' library is required to read Excel files. Please install it using `pip install openpyxl`.")
    st.stop()

# Set up the app
st.set_page_config(page_title="Kashif Ali App", layout="wide")
st.title("💽 Kashif Ali App")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

# File uploader
uploaded_files = st.file_uploader(
    "Upload your files (CSV or Excel):",
    type=["csv", "xlsx"],
    accept_multiple_files=True,
)

if uploaded_files:
    for file in uploaded_files:
        # Get the file extension
        file_ext = file.name.split(".")[-1].lower()

        # Read the file based on its extension
        try:
            if file_ext == "csv":
                df = pd.read_csv(file)  # Read CSV files
            elif file_ext == "xlsx":
                df = pd.read_excel(file, engine="openpyxl")  # Read Excel files
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue
        except Exception as e:
            st.error(f"Error reading file {file.name}: {e}")
            continue

        # Display file info
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")  # File size in KB

        # Show the first 5 rows of the DataFrame
        st.write("Preview the Head of the DataFrame:")
        st.dataframe(df.head())

        # Data cleaning options
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            # Remove duplicates
            if st.button(f"Remove Duplicates from {file.name}"):
                df.drop_duplicates(inplace=True)
                st.write("Duplicates Removed!")

            # Fill missing values
            if st.button(f"Fill Missing Values for {file.name}"):
                numeric_cols = df.select_dtypes(include=["number"]).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.write("Missing Values Have Been Filled!")

        # Select columns to keep
        st.subheader("Select Columns to Keep")
        columns = st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Data visualization
        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            # Check for numeric columns
            numeric_cols = df.select_dtypes(include="number").columns
            if len(numeric_cols) == 0:
                st.warning("No numeric columns found for visualization.")
            else:
                # Let the user choose which numeric column to plot
                selected_column = st.selectbox(
                    f"Select a numeric column to plot for {file.name}",
                    numeric_cols
                )
                # Plot the selected column
                st.line_chart(df[selected_column])

        # File conversion
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

            # Download button
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success("🎉 All Files Processed!")