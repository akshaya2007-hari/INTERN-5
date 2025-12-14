import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model1.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌦️ Weather Prediction App")
st.write("Predict precipitation percentage using temperature")

# Input
temperature = st.number_input(
    "Enter Temperature (°C)",
    min_value=-20.0,
    max_value=60.0,
    step=0.1
)

# Predict
if st.button("Predict"):
    input_data = np.array([[temperature]])
    prediction = model.predict(input_data)[0]

    st.success(f"🌧️ Predicted Precipitation: {prediction:.2f} %")

