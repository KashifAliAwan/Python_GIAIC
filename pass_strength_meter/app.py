import streamlit as st
import re

# Function to evaluate password strength
def evaluate_password_strength(password):
    score = 0

    # Criteria checks
    length_check = len(password) >= 8
    uppercase_check = any(char.isupper() for char in password)
    lowercase_check = any(char.islower() for char in password)
    digit_check = any(char.isdigit() for char in password)
    special_char_check = bool(re.search(r'[!@#$%^&*]', password))

    # Assign scores based on criteria
    if length_check:
        score += 1
    if uppercase_check:
        score += 1
    if lowercase_check:
        score += 1
    if digit_check:
        score += 1
    if special_char_check:
        score += 1

    return score

# Function to provide feedback
def provide_feedback(score, password):
    feedback = []
    if len(password) < 8:
        feedback.append("❌ Make the password at least 8 characters long.")
    if not any(char.isupper() for char in password):
        feedback.append("❌ Include at least one uppercase letter.")
    if not any(char.islower() for char in password):
        feedback.append("❌ Include at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        feedback.append("❌ Include at least one digit.")
    if not re.search(r'[!@#$%^&*]', password):
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if score <= 2:
        strength = "Weak"
        color = "#FF4B4B"  # Red
        icon = "⚠️"
    elif score <= 4:
        strength = "Moderate"
        color = "#FFA500"  # Orange
        icon = "🟡"
    else:
        strength = "Strong"
        color = "#2ECC71"  # Green
        icon = "✅"
        feedback.append("✅ Your password meets all the criteria!")

    return strength, color, icon, feedback

# Streamlit App
def main():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        /* Black background */
        .stApp {
            background-color: #000000;
            color: #FFFF00; /* Yellow text */
            font-family: 'Arial', sans-serif;
        }
        /* Title styling */
        h1 {
            color: #FFFF00; /* Yellow */
            font-family: 'Arial', sans-serif;
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
        }
        /* Card styling */
        .card {
            background: rgba(255, 255, 255, 0.1); /* Semi-transparent white */
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 4px 8px rgba(255, 255, 0, 0.2); /* Yellow shadow */
        }
        /* Input field styling */
        .stTextInput > div > div > input {
            font-size: 18px;
            padding: 12px;
            border-radius: 8px;
            border: 2px solid #FFFF00; /* Yellow border */
            background-color: #000000; /* Black background */
            color: #FFFF00; /* Yellow text */
            width: 100%;
        }
        /* Progress bar styling */
        .stProgress > div > div > div > div {
            background-color: #FFFF00; /* Yellow */
            border-radius: 8px;
        }
        /* Feedback styling */
        .feedback {
            font-size: 16px;
            font-family: 'Arial', sans-serif;
            margin-top: 10px;
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.1); /* Semi-transparent white */
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(255, 255, 0, 0.2); /* Yellow shadow */
            color: #FFFF00; /* Yellow text */
        }
        /* Button styling */
        .stButton > button {
            background-color: #FFFF00; /* Yellow */
            color: #000000; /* Black text */
            font-size: 18px;
            padding: 12px 24px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            width: 100%;
        }
        .stButton > button:hover {
            background-color: #FFD700; /* Gold on hover */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

