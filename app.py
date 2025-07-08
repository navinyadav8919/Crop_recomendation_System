import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('crop_model.pkl', 'rb'))

st.title("🌾 Crop Recommendation System")

st.markdown("Enter the soil and environmental conditions below:")

# Input fields
N = st.number_input('Nitrogen (N)', min_value=0)
P = st.number_input('Phosphorus (P)', min_value=0)
K = st.number_input('Potassium (K)', min_value=0)
temperature = st.number_input('Temperature (°C)')
humidity = st.number_input('Humidity (%)')
ph = st.number_input('pH', min_value=0.0, max_value=14.0, step=0.1)
rainfall = st.number_input('Rainfall (mm)', min_value=0.0)

if st.button('Predict Crop'):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Recommended Crop: **{prediction.upper()}**")
