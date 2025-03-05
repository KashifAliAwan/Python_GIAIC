import streamlit as st

# Custom CSS for styling
st.markdown("""
<style>
    /* Main container */
    .main {
        background-color: #000000; /* Black background */
        color: #39ff14; /* Neon green text */
        padding: 20px;
        border-radius: 10px;
    }
    /* Header */
    .header {
        font-size: 50px;
        font-weight: bold;
    
        color: #39ff14; /* Neon green */
        text-align: center;
        margin-bottom: 20px;
    }
    /* Sidebar */
    .sidebar .sidebar-content {
        background-color: #000000; /* Black background */
        color: #39ff14; /* Neon green text */
        padding: 20px;
        border-radius: 10px;
    }
    /* Buttons */
    .stButton>button {
        background-color: #39ff14; /* Neon green */
        color: #000000; /* Black text */
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #2cc70c; /* Darker neon green on hover */
    }
    /* Social Icons */
    .social-icons {
        display: flex;
        gap: 20px;
        margin-top: 20px;
    }
    .social-icons a {
        color: #39ff14; /* Neon green */
        text-decoration: none;
        font-size: 24px;
    }
    .social-icons a:hover {
        color: #2cc70c; /* Darker neon green on hover */
    }
    /* Links in sidebar */
    .sidebar-links {
        margin-top: 20px;
    }
    .sidebar-links a {
        color: #; /* Neon green */
        text-decoration: none;
    }
    .sidebar-links a:hover {
        color: #2cc70c; /* Darker neon green on hover */
    }
</style>
""", unsafe_allow_html=True)

# Conversion functions
def convert_length(value, from_unit, to_unit):
    units = {
        'meter': 1,
        'centimeter': 0.01,
        'kilometer': 1000,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
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

def convert_time(value, from_unit, to_unit):
    units = {
        'second': 1,
        'millisecond': 0.001,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2628000,  # Approximate
        'year': 31536000  # Approximate
    }
    return value * units[from_unit] / units[to_unit]

# Streamlit App
st.markdown('<div class="header">🧶UNIT CONVERTER</div>', unsafe_allow_html=True)

# Sidebar for additional information
with st.sidebar:
    st.markdown('<div class="sidebar">', unsafe_allow_html=True)
    st.write("**About the App**")
    st.write("This app allows you to convert units for **Length**, **Temperature**, and **Time**. Select a category, enter a value, and choose the units to convert.")
    st.write("---")
    st.write("**Developer Info**")
    st.write("Name: Kashif Ali")
    st.write("Role: Developer")
    st.write("---")
    st.write("**Connect with Me**")
    st.markdown("""
    <div class="sidebar-links">
        <a href="https://github.com/kashifaliawan" target="_blank">
            <i class="fab fa-github"></i> GitHub
        </a>
        <br>
        <a href="https://www.linkedin.com/in/kashif-ali-developer/" target="_blank">
            <i class="fab fa-linkedin"></i> LinkedIn
        </a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

