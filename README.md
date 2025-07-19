# 🌸 Iris Flower Classifier Web App

This Streamlit web application predicts the species of an Iris flower based on user-input sepal and petal measurements. The model is trained using logistic regression and deployed via a simple, user-friendly interface.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://iris-app-app-g2jdtgt8lpamszw6gynwgm.streamlit.app/)

## How to use:
Adjust the sliders on the left (or main page) to input the sepal and petal measurements, and the app will predict the Iris species.
... (rest of your README content) ...


## 🔍 Features

- Predicts one of three Iris species: Setosa, Versicolor, Virginica
- Real-time prediction using logistic regression
- Clean and interactive UI with Streamlit
- Lightweight and fast

## 📁 Project Structure

├── app.py # Streamlit app
├── train_model.py # Model training script
├── model.pkl # Saved trained model


## Technologies Used

* **Python 3.10+**: The core programming language.
* **Streamlit (`streamlit`)**: Version `1.36.0` (or specify your version). Used for building the interactive web application frontend.
* **Scikit-learn (`scikit-learn`)**: Version `1.5.0` (or specify your *actual* model training version). Essential for the machine learning model (e.g., RandomForestClassifier, DecisionTreeClassifier).
* **Pandas (`pandas`)**: Version `2.2.2` (or specify your version). Used for efficient data manipulation and preparing model input.
* **NumPy (`numpy`)**: Version `1.26.4` (often a dependency of pandas/scikit-learn). For numerical operations.


## 🚀 How to Run

Make sure you have Python installed, then run:


pip install streamlit scikit-learn pandas
streamlit run app.py
🧠 Model
Algorithm: Logistic Regression

Dataset: Iris dataset from sklearn.datasets

📌 Requirements
Python 3.x

streamlit

scikit-learn

pandas

Install all dependencies:
pip install -r requirements.txt


✨ Output
Replace with actual screenshot file name if needed 

🛠️ Author
Rosy Mondal
Intern @ Celebal Technologies
LinkedIn: https://www.linkedin.com/in/rosy-mondal/


