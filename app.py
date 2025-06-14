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
with st.expander("💬 Open CareerAI Chatbot"):
    st.components.v1.iframe(
        "https://hf.co/chat/assistant/684d3f7c795c4b019162d4f7",
        height=700,
        width=900
    )
