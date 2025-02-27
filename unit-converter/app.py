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


# Streamlit app
st.title("🎓Unit Converter By Kashif Ali")
st.markdown(
    "📎 This is a simple unit converter app built with Streamlit. You can convert between different units of length, weight, and temperature."
)

# Select conversion type
conversion_type = st.selectbox(
    "Select Conversion Type", ["Length", "Weight", "Temperature"]
)

if conversion_type == "Length":
    units = [
        "meter",
        "kilometer",
        "centimeter",
        "millimeter",
        "inch",
        "foot",
        "yard",
        "mile",
    ]
elif conversion_type == "Weight":
    units = ["gram", "kilogram", "milligram", "pound", "ounce"]
elif conversion_type == "Temperature":
    units = ["celsius", "fahrenheit", "kelvin"]

# Input value and units
value = st.number_input("Enter value", value=1.0)
from_unit = st.selectbox("From unit", units)
to_unit = st.selectbox("To unit", units)

# Perform conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    st.success(f"Converted value: {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.markdown(
    "#### Check out my GitHub profile for more projects:😎 [Kashif Ali Awan](https://github.com/kashifaliawan)"
)
