import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
with open("house_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏠 House Price Predictor (₹ in Lakhs)")

st.sidebar.header("Enter House Details")

# User Inputs
area = st.sidebar.slider("Area (sq. ft.)", 500, 5000, 1000, step=50)
bedrooms = st.sidebar.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.sidebar.selectbox("Number of Bathrooms", [1, 2, 3])
location = st.sidebar.selectbox("Location Type", ["Urban", "Suburban", "Rural"])

st.markdown("### 🔍 Summary of Inputs")
st.write(f"📐 Area: {area} sq.ft.")
st.write(f"🛏️ Bedrooms: {bedrooms}")
st.write(f"🛁 Bathrooms: {bathrooms}")
st.write(f"📍 Location: {location}")

if st.button("📊 Predict Price"):
    input_data = {
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "location": [location]
    }
    prediction = model.predict(pd.DataFrame(input_data))[0]
    st.success(f"💰 Estimated House Price: ₹{prediction:,.2f} Lakhs")
