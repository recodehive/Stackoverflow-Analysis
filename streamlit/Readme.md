# Web Page for StackOverflow Analysis Using Streamlit
* Author: Leena Goyal [@Leena2403](https://www.github.com/Leena2403) and [Nikita](https://github.com/NIKITA320495)
* Created on: May 20, 2024
* Description: Data exploration & visualization on stackoverflow surveys conducted in 2018,2019,2020.
* Curated dataset: Provided by StackOverflow Analysis


#### Main Interface Look  
![](Visualizations/main-interface.png?raw=true)

##Note##
The web app is still under construction. The authors are in the process of updating and bulding the complete web app.

#### Steps To Run Streamlit Locally:
- cloning
  - firstly, fork the repository and then clone to your local files via vs code (for cloning press ctrl + shift + p).
  - ![](Visualizations/cloning-1.png?raw=true)
  - ![](Visualizations/cloning-2.png?raw=true)

- terminal
  - locate the streamlit folder.
  - run the python -m streamlit run home.py in your cmd terminal.
  - ![](Visualizations/terminal.png?raw=true)

# Solutions Provided

- used streamlit along with some html and css to make the whole webpage.

- Made comprehensible and reusable functions for all the visualisations from the Jupyter anlaysis.

- Used plotly for interactive data visualization.
  
- Made a fully functional web page that showcases all the year-wise analysis on a single platform.


# StackOverflow Datasets

The datasets provided and used include 

- *Survey Results Sample 2018*
    - 2018
- *Survey Results Sample 2019*
    - 2019
- *Survey Results Sample 2020*
    - 2020
  

The data ranges from 2018-2020. The goal is to try to bring all the visuals present in the jupyter analysis notebook in one web page, which is easy on the eye to read and understand in one glance. Alongside, creating comprehensive and dynamic functions that can be implemented for the future datasets.

Using Streamlit, the whole web-page has been created. HTML and CSS has also been used for structuring and styling the web page.

## Dataset
Dataset is the surveys that was conducted by StackOverflow Analysis on their online platform. Stack Overflow is the largest, most trusted online community for developers to learn, share​ ​their programming ​knowledge, and build their careers. It was mainly taken by Developers, Students from Engineering Background, Professionals in Technology. The survey asked basic questions from the people like their Operating System, DevType (Backend, Fullstack), Employment status, Job Satisfaction, Education, IDEs, Language they Worked With and much more.

## Interface
- The whole interface has been created using Streamlit, HTML, CSS. Three different categories of visualisations are provided, divided by year 2018 Analysis, 2019 Analysis, 2020 Analysis. For each of the category, comprehensive and useful analysis, plots and maps have been implemented.

- *Streamlit*: Streamlit has been used for making the StackOverflow Analysis web-page. It is very easy to use, and implement for data scientists, in order to clearly see all the visualisations in a single platform without much hassles. We were able to integrate all the main functions present on Jupyter notebook using Streamlit. We made dedicated function for each analysis, and then ran them on Streamlit.

- *HTML*: HTML has been used that provides basic structure to all the analysis columns present in the website. For displaying graphs, Plotly is used. Each and every analysis of the webpages are being organized through divs.

- *CSS*: The overall structuring and design of the website is enhanced with css with proper shaping of the containers, and also the color combination of the webpage.

*Data Preparation for Analysis*

We directly saved the cleaned and preprocessed datasets from the Jupyter Notebook. The few things we changed, such as re-naming column names, have been written in the main-analysis file.

- *Data Extraction*:
  - Survey Results Sample 2018: Unique years present in the FIR dataset.
  - Survey Results Sample 2018: Unique crime numbers present in the FIR dataset.
  - Survey Results Sample 2018: Unique FIR numbers present in the FIR dataset.

## Folders and Files##

*Visualisations*
- [Visualisations](https://github.com/NIKITA320495/Stackoverflow-Analysis/tree/main/streamlit/Visualizations) - it contains some of the visualizations of tha analysis and the graphs. the screenshots of our project and some templates.


*Functions*
- [Functions](https://github.com/NIKITA320495/Stackoverflow-Analysis/blob/main/streamlit/functions.py) - Dedicated functions for all the analyses, and the predictions that are present in the main analysis file of the Jupyter Notebook, are created.
- Most of the functions are using Plotly library for the clear and better visuals.
- These functions are flexible to be used with dataset of any year, given that the pre-processing stage is compatible with the existing dataframes.
- some of the functions are plot_boxplot() for plotting the boxplot , plot_bar_plotly() for plotting the bargraph , plot_age_distribution() for plotting the age distribution , gender_vs _top5countries() for comparing and plotting the gender and top 5 countries respondants , and many more.

*Main Analysis*
- [Main Analysis](https://github.com/NIKITA320495/Stackoverflow-Analysis/blob/main/streamlit/main_analysis.py) - The main visualisations from our web app providing the png files for bar graphs, line plots, and maps.
- The main visualisations from our web app providing the png files for bar graphs, line plots and maps.
- The dedicated explanatory analysis is also present along with their functions.


*Home*
- [Home](https://github.com/NIKITA320495/Stackoverflow-Analysis/blob/main/streamlit/home.py) - The main visualisations from our web app providing the png files for bar graphs, line plots, and maps.
- set the structure of our main interface.
- we made a slidebar that gives an option to select from the year 2018,2019 and 2020.
- It runs different functions based on the year such as if the selected year is 2018 it shows all the visualizations related to year 2018 and same with 2019 and 2020.
  
*Data Visualisations*:

If specific year is selected from the slidebar, it shows all the visualizations according to it.
First of all, it shows the data preview for the specific year, then all the  data visualizations are shown related to that year.
some of the visualizations such as common for the all the year such as Top Gender Distributions, Distribution of Annual Salary for Top Countries, Geographical plot to show number of respondents in each country,Income vs gender, Ethnicity vs participation, gender vs participation,country wise data scientists presentation, Features of job selection, Education level vs salary,etc

# Distribution of annual salary for top countries 
![](Visualizations/annual-salaries.png?raw=true)
![](Visualizations/income-vs-gender.png?raw=true)
![](Visualizations/ethenicity.png?raw=true)
![](Visualizations/geoplot.png?raw=true)

some of the visualizations are for comparing the data from all the year like Distribution of surveyors based on their developer role and  Programming language desired to work

# Distribution of surveyors based on their developer role
![](Visualizations/Screenshot.png?raw=true)

# Programming language desired to work
![](Visualizations/languages-desired.png?raw=true)
