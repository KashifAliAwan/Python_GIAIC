import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    units = {
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }
    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {
        'kilogram': 1,
        'gram': 0.001,
        'milligram': 0.000001,
        'pound': 0.453592,
        'ounce': 0.0283495
    }
    return value * units[from_unit] / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

# Streamlit App
st.title("Unit Converter")

# Category selection
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# Input value
value = st.number_input("Enter Value", value=1.0)

# Unit selection based on category
if category == "Length":
    from_unit = st.selectbox("From Unit", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    to_unit = st.selectbox("To Unit", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    result = convert_length(value, from_unit, to_unit)
elif category == "Weight":
    from_unit = st.selectbox("From Unit", ["kilogram", "gram", "milligram", "pound", "ounce"])
    to_unit = st.selectbox("To Unit", ["kilogram", "gram", "milligram", "pound", "ounce"])
    result = convert_weight(value, from_unit, to_unit)
elif category == "Temperature":
    from_unit = st.selectbox("From Unit", ["celsius", "fahrenheit", "kelvin"])
    to_unit = st.selectbox("To Unit", ["celsius", "fahrenheit", "kelvin"])
    result = convert_temperature(value, from_unit, to_unit)

# Display result
st.success(f"Converted Result: {result:.4f} {to_unit}")