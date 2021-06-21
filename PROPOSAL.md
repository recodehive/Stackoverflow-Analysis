# Project Proposal

## Finding Insights from Stackoverflow Developer Survey

Stack overflow is a professional community for developers, Stackoverflow conducts a survey every year the collected data from 2011 has been available for open source on the web with the latest dataset 2020 released on March 5th, 2021. If the dataset analysed professionally using modern tools, would enable us to answer real-world questions effectively. The dataset has covered 275 questions in total.

### Project Goal:

1. To perform Analysis on 3 years Stackoverflow Dataset and get insights.
2. To perform Data Analysis and answer the below questions.
   + Impact of igher education on salary of the surveyed developers.
   + Impact of education/experience/responsibilities on gender inequalities.
   + Impact on participation rate due to different ethnicity.
   + To find whether there is any difference between men and women's income.
   + Impact on the increase in popularity of a language in the current year due to developer’s interest in the previous year.

3. To perform data visualization on

   - The most commonly used language.

   - Distribution of surveyors based on their developer role.

   - Factors affecting Job satisfaction.

   - Predicting the growth of languages for upcoming years based on the survey answers.

     ###### The Insights can be used to provide information regarding IT environment, hiring employees and job seekers and build a solid résumé.

### Data Source and Background

The dataset is very diverse and came from a [Stackoverflow developer survey](https://insights.stackoverflow.com/survey/?_ga=2.208907280.304952146.1616422967-1864686930.1616422967) with 275 questions answered from 180 countries. Stackoverflow has data collected through surveys from 2011 to 2020, but for the project, the purpose is to analyze the data of the last 3 years. The people who completed the survey mostly from the US, India, and EMEA regions. The majority of the survey respondents had the background of developer/ coding experience. The data are available in the CSV format ranging from 40 to 150 MB with data of 1.5 Lakh survey participants.The dataset includes survey data gathered from 180 countries, the response ranges from Not at all important to very important/ Not at all satisfied to very satisfied. 

### Data Format

The data is in a schema CSV file that consists of 252,199 observations and 62 variables. 

### Projected work needs to be done for Insights.

###### Data Wrangling

**Dealing Null Values**: As this is a developer survey and few questions left unanswered by the respondents as ‘*NA*’ or ‘*Not Applicable*’ so dealing with null values is important to get precise information. Data conversion/ manipulation is also required, as the developer responded to the survey through radio buttons rather than yes or no pattern(Univariate analysis).

###### Techniques expect to use in the project 

Planning to use ML Algorithms like Random, may include, KNN, AUC for classification problems, training model, logistic regression,data visualization, parameter analysis, Linear Regreesion, Root Mean square.

> Linear regression(RFE techniques) 

$$
y = O_1X + O_2
$$

> Root Mean Squared Error Calculations

$$
rmse = \sqrt{(\frac{1}{n})\sum_{i=1}^{n}(y_{i} - x_{i})^{2}}
$$



#### Project plan

**Week 8:** Creating Project base, Source control([GitHub](https://github.com/Sanjayviswa/Stackoverflow_survey_Analysis)), Project Management(MS Project).

- Complete Data Wrangling & basic Analysis.

**Week 10**: Complete baseline Model building with algorithms.

**Week 11:** Run tests and evaluate model.

**Week 12:** Prepare video presentation.

