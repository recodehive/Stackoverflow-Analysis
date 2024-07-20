import streamlit as st
import pandas as pd
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
df = pd.read_csv('IoT-Security-Dataset.csv')

# Load the saved Random Forest model
rf_model_loaded = joblib.load('random_forest_model.pkl')

# Load and fit the TF-IDF vectorizer on the dataset
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
tfidf_vectorizer.fit(df['Cleaned Sentence'])

# Function to preprocess the input text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d', ' ', text)
    text = re.sub(r'\s+[a-z]\s+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Function to predict if a question is security-related
def predict_security(question, model, vectorizer):
    clean_question = preprocess_text(question)
    question_tfidf = vectorizer.transform([clean_question])
    prediction = model.predict(question_tfidf)
    return prediction[0]

# Streamlit app
st.title("Security text Predictor")

st.write("Enter your question below to determine if it is related to security.")

user_question = st.text_area("Your Question")

if st.button("Predict"):
    if user_question.strip() != "":
        prediction = predict_security(user_question, rf_model_loaded, tfidf_vectorizer)
        if prediction == 0:
            st.success("This question is security-related.")
        else:
            st.info("This question is not security-related.")
    else:
        st.error("Please enter a question.")
