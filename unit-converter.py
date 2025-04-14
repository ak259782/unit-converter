import streamlit as st #type: ignore

# Dictionary for unit conversions (Now includes country-specific conversions)
CONVERSIONS = {
    "meter_kilometer": 0.001,
    "kilometer_meter": 1000,
    "gram_kilogram": 0.001,
    "kilogram_gram": 1000,
    "centimeter_meter": 0.01,
    "meter_centimeter": 100,
    "mile_kilometer": 1.60934,
    "kilometer_mile": 0.621371,
    
    # Currency conversion (Example: Rough estimates, use APIs for live rates)
    "usd_pkr": 277.50,  # 1 USD = 277.50 PKR (Example rate)
    "pkr_usd": 0.0036,  # 1 PKR = 0.0036 USD
    "usd_eur": 0.92,  # 1 USD = 0.92 EUR
    "eur_usd": 1.09,  # 1 EUR = 1.09 USD

    # Temperature conversion (Special formula needed, handled separately)
}

# Function to convert units
def convert_units(value, unit_from, unit_to):
    key = f"{unit_from}_{unit_to}"
    
    if key in CONVERSIONS:
        return value * CONVERSIONS[key]
    elif unit_from == "celsius" and unit_to == "fahrenheit":
        return (value * 9/5) + 32
    elif unit_from == "fahrenheit" and unit_to == "celsius":
        return (value - 32) * 5/9
    else:
        return None  # If conversion is not supported

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="🔄")
st.title("🔄 Unit Converter by Areeba")

# User Input
value = st.number_input("Enter the value:", min_value=0.0, step=0.1)
unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram", "centimeter", "mile", "usd", "pkr", "eur", "celsius", "fahrenheit"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram", "centimeter", "mile", "usd", "pkr", "eur", "celsius", "fahrenheit"])

# Convert Button
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    
    if result is None:
        st.error("❌ Conversion not supported between these units!")
    else:
        st.success(f"✅ Converted Value: {result} {unit_to}")

# Footer with name
st.sidebar.markdown("👨‍💻 **Developed by Muhammad Osama**")
st.sidebar.markdown("🌍 **Supports: Distance, Weight, Currency, Temperature**")
