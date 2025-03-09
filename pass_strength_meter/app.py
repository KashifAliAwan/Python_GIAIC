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

