import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        ("Metre", "Centimetre"): 100,
        ("Centimetre", "Metre"): 0.01,
        ("Kilometre", "Metre"): 1000,
        ("Metre", "Kilometre"): 0.001,
        ("Mile", "Kilometre"): 1.609,
        ("Kilometre", "Mile"): 0.621,
    }
    
    return value * conversion_factors.get((from_unit, to_unit), 1)

st.title("Unit Converter")

st.write("Convert between different units of length.")

units = ["Metre", "Centimetre", "Kilometre", "Mile"]

value = st.number_input("Enter value", min_value=0.0, value=1.0)
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

converted_value = convert_units(value, from_unit, to_unit)

st.write(f"**{value} {from_unit} = {converted_value} {to_unit}**")
