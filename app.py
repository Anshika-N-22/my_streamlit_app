import streamlit as st
import requests

st.title("💱 Currency Converter")

amount = st.number_input("Enter amount:", value=1.0)
from_currency = st.selectbox("From", ["USD", "EUR", "INR", "GBP"])
to_currency = st.selectbox("To", ["USD", "EUR", "INR", "GBP"])

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url).json()
    rate = response['rates'][to_currency]
    result = amount * rate
    st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")