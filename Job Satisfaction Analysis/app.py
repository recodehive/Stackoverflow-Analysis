import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the model
model = joblib.load('model.pkl')

# Define the feature columns used in the model
features = ['Hobby', 'OpenSource', 'Country', 'Student', 'Employment', 'FormalEducation',
            'UndergradMajor', 'CompanySize', 'DevType', 'YearsCoding', 'YearsCodingProf']

# Initialize label encoders for categorical features
encoders = {
    'Hobby': LabelEncoder().fit(['Yes', 'No']),
    'OpenSource': LabelEncoder().fit(['Yes', 'No']),
    'Country': LabelEncoder().fit(['United States', 'India', 'Germany']),
    'Student': LabelEncoder().fit(['Yes', 'No']),
    'Employment': LabelEncoder().fit(['Employed full-time', 'Employed part-time', 'Self-employed', 'Unemployed']),
    'FormalEducation': LabelEncoder().fit(["Bachelor’s degree (BA, BS, B.Eng., etc.)", 
                                           "Master’s degree (MA, MS, M.Eng., MBA, etc.)", 
                                           "Doctoral degree (PhD)"]),
    'UndergradMajor': LabelEncoder().fit(["Computer science, computer engineering, or software engineering", 
                                          "Information technology, networking, or system administration", 
                                          "Other engineering discipline"]),
    'CompanySize': LabelEncoder().fit(['Fewer than 10 employees', '10 to 19 employees', '20 to 99 employees', 
                                       '100 to 499 employees', '500 to 999 employees', '1,000 to 4,999 employees']),
    'DevType': LabelEncoder().fit(['Developer, back-end', 'Developer, front-end', 'Developer, full-stack']),
    'YearsCoding': LabelEncoder().fit(['0-2 years', '3-5 years', '6-8 years', '9-11 years']),
    'YearsCodingProf': LabelEncoder().fit(['0-2 years', '3-5 years', '6-8 years', '9-11 years']),
}

st.title('Job Satisfaction Prediction')

# Create a form for user input
with st.form(key='prediction_form'):
    Hobby = st.selectbox('Hobby:', ['Yes', 'No'])
    OpenSource = st.selectbox('Open Source:', ['Yes', 'No'])
    Country = st.selectbox('Country:', ['United States', 'India', 'Germany'])
    Student = st.selectbox('Student:', ['Yes', 'No'])
    Employment = st.selectbox('Employment:', ['Employed full-time', 'Employed part-time', 'Self-employed', 'Unemployed'])
    FormalEducation = st.selectbox('Formal Education:', ["Bachelor’s degree (BA, BS, B.Eng., etc.)", 
                                                         "Master’s degree (MA, MS, M.Eng., MBA, etc.)", 
                                                         "Doctoral degree (PhD)"])
    UndergradMajor = st.selectbox('Undergrad Major:', ["Computer science, computer engineering, or software engineering", 
                                                       "Information technology, networking, or system administration", 
                                                       "Other engineering discipline"])
    CompanySize = st.selectbox('Company Size:', ['Fewer than 10 employees', '10 to 19 employees', '20 to 99 employees', 
                                                 '100 to 499 employees', '500 to 999 employees', '1,000 to 4,999 employees'])
    DevType = st.selectbox('Dev Type:', ['Developer, back-end', 'Developer, front-end', 'Developer, full-stack'])
    YearsCoding = st.selectbox('Years Coding:', ['0-2 years', '3-5 years', '6-8 years', '9-11 years'])
    YearsCodingProf = st.selectbox('Years Coding Professionally:', ['0-2 years', '3-5 years', '6-8 years', '9-11 years'])
    
    submit_button = st.form_submit_button(label='Get Prediction')

if submit_button:
    # Collect user input
    input_data = {
        'Hobby': Hobby,
        'OpenSource': OpenSource,
        'Country': Country,
        'Student': Student,
        'Employment': Employment,
        'FormalEducation': FormalEducation,
        'UndergradMajor': UndergradMajor,
        'CompanySize': CompanySize,
        'DevType': DevType,
        'YearsCoding': YearsCoding,
        'YearsCodingProf': YearsCodingProf
    }
    
    # Convert user input to DataFrame
    input_df = pd.DataFrame([input_data])

    # Encode categorical features
    for feature in features:
        input_df[feature] = encoders[feature].transform(input_df[feature])
    
    # Ensure the input has the same columns as the training data
    input_df = input_df[features]

    # Make prediction
    prediction = model.predict(input_df)

    # Display the prediction
    st.write(f'Predicted Job Satisfaction: {prediction[0]}')
