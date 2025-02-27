import streamlit as st

# Define conversion functions
def convert_length(value, from_unit, to_unit):
    length_conversions = {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34,
    }
   