import streamlit as st

# Define conversion functions and formulas
def convert_length(value, from_unit, to_unit):
    conversions = {
        'meter': 1,
        'kilometer': 0.001,
        'centimeter': 100,
        'millimeter': 1000,
        'inch': 39.3701,
        'foot': 3.28084,
        'yard': 1.09361,
        'mile': 0.000621371
    }
    formula = f"{value} {from_unit} * {conversions[to_unit]} / {conversions[from_unit]}"
    return value * conversions[to_unit] / conversions[from_unit], formula

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'kilogram': 1,
        'gram': 1000,
        'milligram': 1e6,
        'pound': 2.20462,
        'ounce': 35.274
    }
    formula = f"{value} {from_unit} * {conversions[to_unit]} / {conversions[from_unit]}"
    return value * conversions[to_unit] / conversions[from_unit], formula

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        formula = f"({value} * 9/5) + 32"
        return (value * 9/5) + 32, formula
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        formula = f"({value} - 32) * 5/9"
        return (value - 32) * 5/9, formula
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        formula = f"{value} + 273.15"
        return value + 273.15, formula
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        formula = f"{value} - 273.15"
        return value - 273.15, formula
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        formula = f"({value} - 32) * 5/9 + 273.15"
        return (value - 32) * 5/9 + 273.15, formula
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        formula = f"({value} - 273.15) * 9/5 + 32"
        return (value - 273.15) * 9/5 + 32, formula
    else:
        return value, "No conversion needed"

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .main {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
        }
        h1 {
            color: #4A90E2;
        }
        .stButton>button {
            background-color: #4A90E2;
            color: white;
            font-size: 16px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #357ABD;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📏 Unit Converter")
st.write("🔄 Convert between different units easily!")

# Sidebar for unit selection
unit_type = st.sidebar.selectbox("⚙️ Select Unit Type", ["📏 Length", "⚖️ Weight", "🌡️ Temperature"])

if unit_type == "📏 Length":
    units = ['meter', 'kilometer', 'centimeter', 'millimeter', 'inch', 'foot', 'yard', 'mile']
elif unit_type == "⚖️ Weight":
    units = ['kilogram', 'gram', 'milligram', 'pound', 'ounce']
elif unit_type == "🌡️ Temperature":
    units = ['celsius', 'fahrenheit', 'kelvin']

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("🔽 Convert From", units)
    value = st.number_input("💡 Enter Value", value=1.0)

with col2:
    to_unit = st.selectbox("🔼 Convert To", units)

if st.button("🚀 Convert Now"):
    if unit_type == "📏 Length":
        result, formula = convert_length(value, from_unit, to_unit)
    elif unit_type == "⚖️ Weight":
        result, formula = convert_weight(value, from_unit, to_unit)
    elif unit_type == "🌡️ Temperature":
        result, formula = convert_temperature(value, from_unit, to_unit)

    st.success(f"✅ Converted Value: {result:.2f} {to_unit}")
    st.info(f"🧮 Conversion Formula: {formula}")

    #Custom CSS
st.markdown("""
    <style>
    /* Main Page Background */
    .main {
        background-color: #E3F2FD; /* Cool Mist Blue */
        padding: 20px;
    }
    
    /* Sidebar Background & Text */
    .stSidebar {
        background-color:rgb(95, 139, 170); /* Deep Indigo */
        color: white;
    }
    .stSidebar h1, .stSidebar h2, .stSidebar h3 {
        color:rgb(250, 158, 130); /* Vibrant Orange */
    }
    
    /* Buttons */
    .stButton>button {
        background-color:rgb(95, 139, 170); /* Royal Purple */
        color: white;
        border-radius: 8px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #6A1B9A; /* Rich Plum */
    }
    
    /* Text Input */
    .stTextInput>div>div>input {
        background-color: #263238; /* Midnight Gray */
        color: white;
        border-radius: 5px;
    }
    
    /* Success Messages */
    .stSuccess {
        background-color:rgb(112, 236, 118); /* Lush Green */
        color: white;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("🚀 Made with ❤ by Khanzadi Wazir Ali")