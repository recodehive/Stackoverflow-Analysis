import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc

# Load the model
model = joblib.load('model.pkl')

# Define the feature columns used in the model
features = ['Hobby', 'OpenSource', 'Country', 'Student', 'Employment', 'FormalEducation',
            'UndergradMajor', 'CompanySize', 'DevType', 'YearsCoding', 'YearsCodingProf']

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

    # Ensure the input has the same columns as the training data
    input_df = input_df[features]

    # Make prediction
    prediction = model.predict(input_df)

    # Display the prediction
    st.write(f'Predicted Job Satisfaction: {prediction[0]}')

    # Evaluate the model on test data (assuming y_test and y_pred are available)
    # This part would typically be done during model development, not in the prediction app
    # However, for demonstration purposes, we can create some dummy data
    y_test = [1, 0, 1, 1, 0]  # Example true labels
    y_pred = model.predict(input_df)  # Example predicted labels

    # Print accuracy
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f'Accuracy: {accuracy:.2f}')

    # Print classification report
    report = classification_report(y_test, y_pred, output_dict=True)
    st.write('Classification Report:')
    st.write(report)

    # Convert classification report to a DataFrame for better readability
    report_df = pd.DataFrame(report).transpose()
    st.write(report_df)

    # Plot confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    st.pyplot(plt)

    # If the model is a binary classifier, plot the ROC curve
    if len(set(y_test)) == 2:
        fpr, tpr, _ = roc_curve(y_test, y_pred)
        roc_auc = auc(fpr, tpr)
        
        plt.figure(figsize=(10, 6))
        plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend(loc='lower right')
        st.pyplot(plt)
