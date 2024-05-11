# Project Proposal

## Finding Insights from Stack Overflow Developer Survey

Stack Overflow is a professional community for developers, conducting an annual survey. The collected data from 2011 onwards has been available for open source on the web, with the latest dataset released in 2020. Analyzing this dataset professionally using modern tools would enable us to answer real-world questions effectively. The dataset includes responses to 275 questions.

### Project Goal:

1. **Perform Analysis on 3 years of Stack Overflow Dataset:** Extract insights from the data.
2. **Data Analysis Goals:** Answer the following questions:
   - What is the impact of higher education on the salary of surveyed developers?
   - How do education, experience, and responsibilities affect gender inequalities?
   - How does ethnicity impact participation rates?
   - Is there a difference in income between men and women?
   - How does the previous year's interest in a language affect its popularity in the current year?
3. **Data Visualization Goals:**
   - Identify the most commonly used language.
   - Analyze the distribution of surveyors based on their developer roles.
   - Explore factors affecting job satisfaction.
   - Predict the growth of languages for upcoming years based on survey answers.
   - Provide insights for IT environment, hiring employees, job seekers, and building a solid résumé.

### Data Source and Background

The dataset is sourced from the annual Stack Overflow developer survey, covering responses from developers in 180 countries. The data range from 2011 to 2020, with the focus being on the last 3 years. Respondents primarily come from the US, India, and EMEA regions, with a background in developer/coding experience. The dataset includes survey data gathered from 180 countries, with responses ranging from "Not at all important" to "Very important" and "Not at all satisfied" to "Very satisfied."

### Data Format

The data is in CSV format, consisting of 252,199 observations and 62 variables.

### Projected Work for Insights

#### Data Wrangling

- **Dealing with Null Values:** Handle unanswered questions marked as ‘NA’ or ‘Not Applicable’ to ensure precise analysis.
- **Data Conversion/Manipulation:** Convert data for analysis, considering that respondents answered the survey through radio buttons rather than yes or no patterns (Univariate analysis).

#### Techniques Expected to Use in the Project

- ML Algorithms: Utilize algorithms like Random Forest, KNN, AUC for classification problems, logistic regression, and linear regression.
- Data Visualization: Employ data visualization techniques for better understanding and presentation of insights.
- Parameter Analysis: Analyze parameters to fine-tune models and improve accuracy.

#### Project Plan

**Week 8:** Project Base Setup
- Source control setup on [GitHub](https://github.com/Sanjayviswa/Stackoverflow_survey_Analysis)
- Project Management using tools like MS Project
- Complete Data Wrangling & Basic Analysis

**Week 10:** Baseline Model Building
- Implement algorithms and build baseline models

**Week 11:** Model Evaluation
- Run tests and evaluate the performance of models

**Week 12:** Finalization
- Prepare video presentation summarizing the analysis and insights

#### Additional Technical Details

**Linear Regression (RFE techniques)**
- Equation: \( y = O_1X + O_2 \)

**Root Mean Squared Error (RMSE) Calculations**
- Formula: \( rmse = \sqrt{\left(\frac{1}{n}\right)\sum_{i=1}^{n}(y_{i} - x_{i})^{2}} \)

Crafted by @Sanjayviswa.
