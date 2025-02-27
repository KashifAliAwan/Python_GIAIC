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
    return value * (length_conversions[from_unit] / length_conversions[to_unit])


def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        "gram": 1.0,
        "kilogram": 1000.0,
        "milligram": 0.001,
        "pound": 453.592,
        "ounce": 28.3495,
    }
    return value * (weight_conversions[from_unit] / weight_conversions[to_unit])


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9 / 5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5 / 9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9 / 5 + 32
    else:
        return value


