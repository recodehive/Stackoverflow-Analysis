import os
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns

# Define the path to the data file
file_path = 'survey_results_sample_2018.csv'

# Check if the file exists
if not os.path.exists(file_path):
    st.error(f"File not found: {file_path}. Please ensure the file is in the correct directory.")
else:
    try:
        # Try to load the dataset
        data = pd.read_csv(file_path)

        # Define the necessary columns
        columns = ['Employment', 'FormalEducation', 'CompanySize', 'DevType', 'Exercise', 'Age', 'OpenSource']
        data = data[columns].copy()

        # Map age values to numerical values
        age_mapping = {
            'Under 18 years old': 0,
            '18 - 24 years old': 1,
            '25 - 34 years old': 2,
            '35 - 44 years old': 3,
            '45 - 54 years old': 4,
            '55 - 64 years old': 5,
            '65 years or older': 6
        }
        data['Age'] = data['Age'].map(age_mapping)

        # Define target variable and feature columns
        target_variable = 'OpenSource'
        categorical_features = ['Employment', 'FormalEducation', 'CompanySize', 'DevType', 'Exercise', 'Age']
        numerical_features = []

        # Preprocessing for categorical data
        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
            ]
        )

        # Split the data
        X = data.drop(target_variable, axis=1)
        y = data[target_variable]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and train the model
        model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', RandomForestClassifier(random_state=42))
        ])
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        classification_rep = classification_report(y_test, y_pred, zero_division=1)
        roc_auc = roc_auc_score(pd.get_dummies(y_test).values[:, 1], model.predict_proba(X_test)[:, 1])

        # Get feature importance
        importances = model.named_steps['classifier'].feature_importances_
        feature_names = list(model.named_steps['preprocessor'].transformers_[0][1].get_feature_names_out())
        feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances}).sort_values(by='Importance', ascending=False)

        # Streamlit App
        st.title('Machine Learning Model Evaluation')

        # Show classification report
        st.header('Classification Report')
        st.text(classification_rep)

        # Show ROC-AUC Score
        st.header('ROC-AUC Score')
        st.text(f"ROC-AUC Score: {roc_auc:.2f}")

        # Plot confusion matrix
        st.header('Confusion Matrix')
        cm = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'], ax=ax)
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        st.pyplot(fig)

        # Plot ROC Curve
        st.header('ROC Curve')
        y_test_binary = pd.get_dummies(y_test).values[:, 1]  # Convert to binary
        fpr, tpr, _ = roc_curve(y_test_binary, model.predict_proba(X_test)[:, 1])
        roc_auc = auc(fpr, tpr)
        fig, ax = plt.subplots()
        ax.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
        ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('ROC Curve')
        ax.legend(loc='lower right')
        st.pyplot(fig)

        # Plot feature importance
        st.header('Feature Importance')
        fig, ax = plt.subplots()
        sns.barplot(x='Importance', y='Feature', data=feature_importance_df.head(20), palette='viridis', ax=ax)
        ax.set_title('Top Feature Importances')
        ax.set_xlabel('Importance')
        ax.set_ylabel('Feature')
        st.pyplot(fig)

        # Section for new data input and prediction
        st.header('Predict for New Data')

        # Input fields for new data
        employment = st.selectbox('Employment', data['Employment'].unique())
        education = st.selectbox('Formal Education', data['FormalEducation'].unique())
        company_size = st.selectbox('Company Size', data['CompanySize'].unique())
        dev_type = st.selectbox('Dev Type', data['DevType'].unique())
        exercise = st.selectbox('Exercise', data['Exercise'].unique())
        age = st.selectbox('Age', list(age_mapping.keys()))

        # Convert inputs to dataframe
        new_data = pd.DataFrame({
            'Employment': [employment],
            'FormalEducation': [education],
            'CompanySize': [company_size],
            'DevType': [dev_type],
            'Exercise': [exercise],
            'Age': [age_mapping[age]]
        })

        # Handle any NaN values
        new_data = new_data.fillna('')

        # Predict the output for new data
        if st.button('Predict'):
            try:
                prediction = model.predict(new_data)
                prediction_prob = model.predict_proba(new_data)[:, 1]
                st.write(f'Prediction: {"Yes" if prediction[0] == "Yes" else "No"}')
                st.write(f'Prediction Probability: {prediction_prob[0]:.2f}')
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

        # ================== EDA Enhancements ==================
        st.header('Enhanced Exploratory Data Analysis (EDA)')

        # Load full dataset for EDA
        eda_data = pd.read_csv(file_path)

        # Salary Analysis
        st.subheader('Salary Distribution')
        eda_data['ConvertedSalary'] = pd.to_numeric(eda_data['ConvertedSalary'], errors='coerce')
        fig, ax = plt.subplots()
        sns.histplot(eda_data['ConvertedSalary'].dropna(), kde=True, ax=ax)
        ax.set_title('Distribution of Salaries')
        ax.set_xlabel('Salary (USD)')
        st.pyplot(fig)

        # Job Satisfaction Analysis
        satisfaction_cols = ['JobSatisfaction', 'CareerSatisfaction']
        for col in satisfaction_cols:
            st.subheader(f'Distribution of {col}')
            fig, ax = plt.subplots()
            eda_data[col].value_counts().plot(kind='bar', ax=ax)
            ax.set_title(f'Distribution of {col}')
            ax.set_xlabel('Satisfaction Level')
            ax.set_ylabel('Count')
            st.pyplot(fig)

        # Programming Languages Analysis
        st.subheader('Top 10 Programming Languages')
        languages = eda_data['LanguageWorkedWith'].str.split(';', expand=True).stack()
        fig, ax = plt.subplots()
        languages.value_counts().head(10).plot(kind='bar', ax=ax)
        ax.set_title('Top 10 Programming Languages')
        ax.set_xlabel('Language')
        ax.set_ylabel('Count')
        st.pyplot(fig)

        # Job Satisfaction by Company Size
        st.subheader('Job Satisfaction by Company Size')
        fig, ax = plt.subplots()
        sns.boxplot(x='CompanySize', y='JobSatisfaction', data=eda_data, ax=ax)
        ax.set_title('Job Satisfaction by Company Size')
        ax.set_xlabel('Company Size')
        ax.set_ylabel('Job Satisfaction')
        st.pyplot(fig)

        # Age Distribution
        st.subheader('Age Distribution of Respondents')
        fig, ax = plt.subplots()
        sns.histplot(eda_data['Age'], kde=True, ax=ax)
        ax.set_title('Age Distribution of Respondents')
        ax.set_xlabel('Age')
        st.pyplot(fig)

        # Top 10 Countries of Respondents
        st.subheader('Top 10 Countries of Respondents')
        country_counts = eda_data['Country'].value_counts().head(10)
        fig, ax = plt.subplots()
        ax.plot(country_counts.index, country_counts.values, marker='o')
        ax.set_title('Top 10 Countries of Respondents')
        ax.set_xlabel('Country')
        ax.set_ylabel('Number of Respondents')
        st.pyplot(fig)

        # Employment Status Distribution
        st.header("Employment Status Distribution")
        employment_counts = eda_data['Employment'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(employment_counts.values, labels=employment_counts.index, autopct='%1.1f%%')
        ax.set_title('Employment Status Distribution')
        ax.axis('equal')
        st.pyplot(fig)

        # Databases Used
        st.header("Top 10 Databases Used")
        databases = eda_data['DatabaseWorkedWith'].str.split(';', expand=True).stack()
        db_counts = databases.value_counts().head(10)
        fig, ax = plt.subplots()
        db_counts.plot(kind='barh', ax=ax)
        ax.set_xlabel('Number of Users')
        ax.set_ylabel('Database')
        st.pyplot(fig)

        # Job Satisfaction by Gender
        st.header("Job Satisfaction by Gender")
        job_sat_gender = pd.crosstab(eda_data['JobSatisfaction'], eda_data['Gender'])
        fig, ax = plt.subplots()
        job_sat_gender.plot(kind='bar', ax=ax)
        ax.set_title('Job Satisfaction by Gender')
        ax.set_xlabel('Job Satisfaction Level')
        st.pyplot(fig)

        # Correlation Heatmap
        st.header("Correlation Heatmap of Numeric Variables")
        numeric_columns = eda_data.select_dtypes(include=['int64', 'float64']).columns
        fig, ax = plt.subplots()
        sns.heatmap(eda_data[numeric_columns].corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title('Correlation Heatmap of Numeric Variables')
        st.pyplot(fig)

        # Cumulative Distribution
        st.header(f"Cumulative Distribution of {numeric_columns[0]}")
        fig, ax = plt.subplots()
        sns.ecdfplot(data=eda_data, x=numeric_columns[0], ax=ax)
        ax.set_title(f'Cumulative Distribution of {numeric_columns[0]}')
        ax.set_xlabel(numeric_columns[0])
        ax.set_ylabel('Cumulative Proportion')
        st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred while loading data: {e}")
