import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🌼 Iris Flower Prediction App")

st.write("Adjust the sliders to predict the type of Iris flower:")

# Input sliders
sepal_length = st.slider("Sepal Length", 4.0, 8.0)
sepal_width = st.slider("Sepal Width", 2.0, 4.5)
petal_length = st.slider("Petal Length", 1.0, 7.0)
petal_width = st.slider("Petal Width", 0.1, 2.5)

# Combine input
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)
probs = model.predict_proba(input_data)

st.subheader(f"🌸 Predicted Species: {prediction[0]}")
st.subheader("Prediction Confidence:")
st.bar_chart(probs[0])
