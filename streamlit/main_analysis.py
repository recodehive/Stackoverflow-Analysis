import streamlit as st
import pandas as pd
import plotly.express as px
import functions as ff

data = pd.read_csv('https://raw.githubusercontent.com/Recode-Hive/Stackoverflow-Analysis/main/streamlit/df2020.csv')
df2018 = pd.read_csv('https://raw.githubusercontent.com/Recode-Hive/Stackoverflow-Analysis/main/streamlit/df2018.csv')
full_data2018 = pd.read_csv('https://raw.githubusercontent.com/Recode-Hive/Stackoverflow-Analysis/main/streamlit/survey_results_sample_2018.csv')
full_data2019=pd.read_csv('https://raw.githubusercontent.com/Recode-Hive/Stackoverflow-Analysis/main/streamlit/survey_results_sample_2019.csv')
full_df2020 = pd.read_csv('https://raw.githubusercontent.com/Recode-Hive/Stackoverflow-Analysis/main/streamlit/survey_results_sample_2020.csv')
df2019 = pd.read_csv('https://raw.githubusercontent.com/Recode-Hive/Stackoverflow-Analysis/main/streamlit/df2019.csv')
df2021 = pd.read_csv('df2021.csv')
df2022 = pd.read_csv('df2022.csv')
df2020 = data[(data['SalaryUSD'] < 200000)]

# Changes made in df2021 and df2022:
# ResponseId = Respondents
# CompTotal = SalaryUSD
# LanguageWantToWorkWith = LanguageDesireNextYear

# features for job satisfaction
results = pd.read_csv("https://raw.githubusercontent.com/Recode-Hive/Stackoverflow-Analysis/main/streamlit/results.csv")

# for hightest paying ds
full_data2018.rename(columns={'ConvertedSalary': 'SalaryUSD'}, inplace=True)

def main_analysis(df):
    st.title("StackOverflow Survey Analysis")

    with st.expander("Data Preview"):
        st.markdown(
            """
            <div style='border-bottom: 4px solid lightblue;'>
                <style>
                .stTable { border-bottom:  4px solid lightblue; }
                </style>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.dataframe(df)

    col_start1, col_start2, col_start3 = st.columns((1,1,1))

    if df is not df2021 and df is not df2022:
        with col_start1:
            ff.plot_pie_plotly(df, 'Gender', 3, 450, 500)
        with col_start2:
            ff.plot_pie_plotly(df, 'Employment', 3, 450, 520)
        with col_start3:
            ff.plot_pie_plotly(df, 'DevType', 3, 450, 500)    

    plots = ff.generate_normal_distribution_plots(df, 'Country',top_n=3)

    col_start1.plotly_chart(next(plots))
    col_start2.plotly_chart(next(plots))
    col_start3.plotly_chart(next(plots))

    annual_salary_top_text = """
    <div class='analysis-container-extra'>
        <div class='analysis-title'>Analysis: Distribution of Annual Salary for Top Countries</div>
        <div class='analysis-text' style="color: red; font-weight: bold;">
            Overall, the country which has the highest mean annual salary is the United States of America(240,000) Dollars. The second highest country which provides the highest mean salary is Australia(164,926) Dollars. Though India has a higher number of respondents, it has the lowest mean salary of $25,213.We can understand that the mean salary of a developed country is much higher than that of a developing country.
        </div>
    </div>
"""
    st.markdown(annual_salary_top_text, unsafe_allow_html=True)

    visual, analysis = st.columns((3,1))
    
    with visual:
        st.title("Geographical Plot For Respondents")
        ff.generate_choropleth(df, 'Respondents')

    with analysis:
        geographical_text = """
    <div class='analysis-container'>
        <div class='analysis-title'>Analysis: Geographical plot to show number of respondents in each country</div>
        <div class='analysis-text' style="color: red; font-weight: bold;">
            The geographical plot shows the number of respondents by country, with the United States having the highest participation. Other countries with significant participation include India, Brazil, and several European nations. The intensity of color represents the number of respondents, with darker shades indicating higher numbers.
        </div>
    </div>
"""
        st.markdown(geographical_text, unsafe_allow_html=True)

    with visual:
        st.title("Income VS Gender")
        figBoxPlot = px.box(df, x='Gender', y='SalaryUSD', title='Income vs Gender')
        st.plotly_chart(figBoxPlot, use_container_width=True)

    with analysis:
        income_gender_text = """
        <div class='analysis-container'>
            <div class='analysis-title'>Analysis: Income vs Gender</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                There is a little bit of difference between Gender and income they received respectively. 
                Men tend to receive more salary than women from the above analysis.
            </div>
        </div>
        """
        st.markdown(income_gender_text, unsafe_allow_html=True)


    with visual:
        st.title("Ethnicity VS Participation")
        ff.plot_bar_plotly(df, 'Ethnicity')

    with analysis:
        Ethnicity_text = """
        <div class='analysis-container'>
            <div class='analysis-title'>Analysis: Ethnicity vs Participation</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                From the Survey Analysis, more participation has been happened from White or of European Ethnicity.
                The least has been recorded as only 0.16% from Indigenous. The second top survey contributors are from South Asians which is 11.93% of the respondents..
            </div>
        </div>
    """
        st.markdown(Ethnicity_text, unsafe_allow_html=True)

    if (df is df2019 or df is df2020):
        with visual:
            st.title("Distribution of Age of Respondents")
            ff.plot_age_distribution(df, 'Age')

        with analysis:
            age_text = """
            <div class='analysis-container-extra'>
                <div class='analysis-title'>Analysis: Distribution of respondents based on age</div>
                <div class='analysis-text' style="color: red; font-weight: bold;">
                    Late twenties respondents are clearly dominating the survey responses. It could be the age-range of a typical user on StackOverflow website.
                    The graph is plotted in a descending order for better visuality, and understanding.
            </div>
        """
            st.markdown(age_text, unsafe_allow_html=True)

    with visual:
        st.title("Men vs Women Participation in Countries with Highest Respondents")
        st.plotly_chart(ff.gender_vs_top5countries(df))

    with analysis:
        gender_top_country_text = """
    <div style='margin-top: 400px !important' class='analysis-container'>
        <div class='analysis-title'>Analysis: Men vs Women Participation</div>
        <div class='analysis-text' style="color: red; font-weight: bold;">
            Women participation is extremely low in the STEM field, compared to men. They are even less than 20% of total male population that is dominating the tech industry in almost all the countries.
        </div>
    </div>
"""     
        st.markdown(gender_top_country_text, unsafe_allow_html=True)      

    st.title("Education Level VS Salary")
    plots = ff.generate_normal_distribution_plots(df, 'EdLevel',top_n=6)

    col_1, col_2, col_3 = st.columns((1, 1, 1))

    col_1.plotly_chart(next(plots))
    col_2.plotly_chart(next(plots))
    col_3.plotly_chart(next(plots))
    col_1.plotly_chart(next(plots))
    col_2.plotly_chart(next(plots))
    col_3.plotly_chart(next(plots))

    education_salary_text = """
            <div class='analysis-container-extra'>
                <div class='analysis-title'>Analysis: Education Levels with Salary Levels</div>
                <div class='analysis-text' style="color: red; font-weight: bold;">
                    As we can see, the respondents who have done Doctorate have the highest mean salary among all other education levels. Secondly, the respondents who have done Bachelors degree have more salary than that of Masters degree holders. This may be due to years of professional coding experience and due to the higher number of respondents in that category than that of Masters degree
                    <br>The most interesting is that the respondents who do not have any degree have a mean salary of $90k. This shows the improvement in online learning and advancement of technology that is shifting the company from relying on University degrees.
            </div>
        """
    st.markdown(education_salary_text, unsafe_allow_html=True)

    ds = full_data2018[full_data2018.reset_index()['DevType'].str.contains('Data scientist or machine learning specialist') == True]
    ds = ds.reset_index(drop=True) 

    if ds is not None: 
        with visual:
            st.title("Country Wise Data Scientists Participation")
            ff.plot_bar_plotly(ds, "Country")

        with analysis:     
            data_scientist_participation_text = """
            <div style='margin-top: 400px !important' class='analysis-container'>
                <div class='analysis-title'>Analysis: Data Scientist Market</div>
                <div class='analysis-text' style="color: red; font-weight: bold;">
                    There are many data scientists who responded to the Stackoverflow survey. Most data scientists are from the US around 1,500-1700 people and it is 3 times higher than data scientists from India. Followed by Germany and the UK with 427 and 339 people respectively. The rest are Canada, France, Netherlands, Brazil, Russia, and Australia which have less than 200 data scientists.
                </div>
            </div>"""


            st.markdown(data_scientist_participation_text, unsafe_allow_html=True)

     

########################################################################
##### To Speed Up the Web Page, Main Analysis is divided into 2 ######


def main_analysis_2(df):
    visual2, analysis2 = st.columns((3,1))

    if df is df2019:
        with visual2:
            ff.plot_bar_plotly(df, 'JobSatisfaction')   

        with analysis2:
              jobsatis_text = """
    <div style='margin-top: 400px !important' class='analysis-container'>
        <div class='analysis-title'>Analysis: Data Scientist Market</div>
        <div class='analysis-text' style="color: red; font-weight: bold;">
            In 2019, the top three countries which have a highest mean annual salary of a data scientist are Ireland (275,851), Luxembourg (272,769), and the USA (265,211). Apart from that, the mean salary of the rest of the countries is less than (200,000) per year. Japan provides the highest mean annual salary among Asian countries (118,969)
            Figures in Dollars $
        </div>
    </div>
"""     
        st.markdown(jobsatis_text, unsafe_allow_html=True) 
    
    with visual2:    
        st.title("Comparing Language Preferences Across Years")
        ff.compare_column_and_plot("LanguageDesireNextYear")

    with analysis2:    
        LanguageDesireNextYear_text = """
        <div class='analysis-container'>
            <div class='analysis-title'>Analysis: Programming language desired to work</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                In 2019, respondents said that they wanted to work in javascript is around more than 10 % and the fewer respond have a desire to work on VBA next year. People started to work in Haskell, Julia, and pearl in 2019 though the amount was less around 5% of people have the desire to work in those languages in 2021. Here, python is the 2nd one in which people have the desire to work in both 2019 and 2020.
                <br>However, if we look at the big picture, Python has been constantly gaining significant popularity within the developers community for three consequent years, whereas JavaScript is either constant or decling in popularity.
        </div>
    """
        st.markdown(LanguageDesireNextYear_text, unsafe_allow_html=True)

    with visual2:
        st.title("Distribution of surveyors based on their developer role")
        ff.compare_column_and_plot("DevType")

    with analysis2:   
        devtype_text = """
        <div style='margin-top: 400px !important' class='analysis-container'>
            <div class='analysis-title'>Analysis: Distribution of surveyors based on their developer role</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                Based on respondents responses the survey concluded that they wanted to work in JavaScript is around more than 10%, and fewer respondents have a desire to work on VBA next year. People started to work in Haskell, Julia, and Pearl in 2019, though the amount was less; around 5% of people have the desire to work in those languages in 2021. Here, Python is the 2nd one in which people have the desire to work in both 2019 and 2020.
                <br>However, if we look at the big picture, Python has been constantly gaining significant popularity within the developer community for three consequent years, whereas JavaScript is either constant or declining in popularity.
            </div>
        </div>
    """
        st.markdown(devtype_text, unsafe_allow_html=True)


    ds = None

    if df is df2019:
        ds = df2019[df2019.reset_index()['DevType'].str.contains('Data scientist or machine learning specialist') == True]
        ds = ds.reset_index(drop=True)
    elif df is df2020:
        ds = df2020[df2020['DevType'].str.contains('Data scientist or machine learning specialist') == True ]
        ds = ds.reset_index(drop=True)   
    else:
        ds = full_data2018[full_data2018.reset_index()['DevType'].str.contains('Data scientist or machine learning specialist') == True]
        ds = ds.reset_index(drop=True) 

    if ds is not None: 
        with visual2:
            st.title("Country Wise Data Scientists Participation")
            ff.plot_bar_plotly(ds, "Country")

        with analysis2:     
            data_scientist_participation_text = """
            <div style='margin-top: 400px !important' class='analysis-container'>
                <div class='analysis-title'>Analysis: Data Scientist Market</div>
                <div class='analysis-text' style="color: red; font-weight: bold;">
                    There are many data scientists who responded to the Stackoverflow survey. Most data scientists are from the US around 1,500-1700 people and it is 3 times higher than data scientists from India. Followed by Germany and the UK with 427 and 339 people respectively. The rest are Canada, France, Netherlands, Brazil, Russia, and Australia which have less than 200 data scientists.
                </div>
            </div>"""


            st.markdown(data_scientist_participation_text, unsafe_allow_html=True)


    # finding top paying countries for data scientists
    '''if df is df2019:
        with visual2:
            st.title("Highest Paying Countries for Data Scientists")
            ff.heighest_paying_2019()
    elif df is df2020:
        with visual2:
            st.title("Highest Paying Countries for Data Scientists")
            ff.heighest_paying(df)
    else:
        with visual2:
            st.title("Highest Paying Countries for Data Scientists")
            ff.heighest_paying(full_data2018)

    with analysis2:
        highest_paying_ds_text = """
    <div style='margin-top: 400px !important' class='analysis-container'>
        <div class='analysis-title'>Analysis: Data Scientist Market</div>
        <div class='analysis-text' style="color: red; font-weight: bold;">
            The top  countries which have a highest mean annual salary of a data scientist are South Korea (253,315) in 2018,Ireland (275,851) in 2019, and the USA(118,863) in 2020. Apart from that, the mean salary of the rest of the countries is less than (200,000) per year. Japan provides the highest mean annual salary among Asian countries (118,969)
            Figures in Dollars $
        </div>
    </div>
"""
        st.markdown(highest_paying_ds_text, unsafe_allow_html=True)'''
    

    with visual2:
        st.title("Features for Job Satisfaction")
        ff.result_plot(results)
    with analysis2:
        feature_jobsatis_text = """
    <div style='margin-top: 400px !important' class='analysis-container'>
        <div class='analysis-title'>Analysis: Features for Job Satisfaction</div>
        <div class='analysis-text' style="color: red; font-weight: bold;">
            The top 2 features negatively affecting Job Satisfaction are age, country. So, in the elderly ages, job satisfaction may decrease because of the personal expectation increases. In the same way, as the professional coding years are increasing, satisfaction may decrease.
            Among the countries; most dissatisfied countries are Angolia, Rwanda, Krygyzstan, Sudan.
            UndergradMajor and other Science, are mostly satisfied.
            Most satisfied countries Malta, Ghana, Cyprus.
        </div>
    </div>
"""     
        st.markdown(feature_jobsatis_text, unsafe_allow_html=True)

def common_analysis_2021_2022(df):
    visual3, analysis3 = st.columns((3,1))

    with visual3:
        fig = ff.plot_comparison_plotly(df,'DevType','SalaryUSD',10,450,700)
        st.plotly_chart(fig)

    with analysis3:
        employment_text = """
        <div class='analysis-container'>
            <div class='analysis-title'>Analysis: DevType VS Salary</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                Full-time developers are unsurprisingly the highest earners based on our bar graph.
                Analysing the graph, fulltime students grap the second spot.
        </div>
    """
        st.markdown(employment_text, unsafe_allow_html=True)
    
    with visual3:
        ff.heighest_paying(df)

    with analysis3:
        highest_paying = """
        <div class='analysis-container'>
            <div class='analysis-title'>Analysis: Highest Paying Data Scientist Countries</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                The top three countries which have a highest mean annual salary of a data scientist are provided using the bar graph. Apart from that, the mean salary of the rest of the countries is less than (200,000) per year. Japan provides the highest mean annual salary among Asian countries (118,969)
            Figures in Dollars $
        </div>
    """
        st.markdown(highest_paying, unsafe_allow_html=True)

    with visual3:
        ff.plot_bar_plotly(df, 'Employment', top_n=10, height=500, width=1000)

    with analysis3:
        employment_text = """
        <div class='analysis-container'>
            <div class='analysis-title'>Analysis: Employment VS Salary</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                Full-time developers are unsurprisingly the highest earners based on our bar graph.
    #             Analysing the graph, fulltime students grap the second spot.
        </div>
    """
        st.markdown(employment_text, unsafe_allow_html=True)

    with visual3:
        ff.plot_bar_plotly(df, 'DevType', top_n=10, height=500, width=1000)

    with analysis3:
        devtype_text = """
        <div class='analysis-container'>
            <div class='analysis-title'>Analysis: DevType VS Respondents</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                Full-stack developers have always dominated the respondents, and this year was no different either.
                Backend developers are following the full-stack. From the graph we can easily see that most of the developers are from full-stack developer, with many niche industry still waiting to be tapped into.
        </div>
    """
        st.markdown(devtype_text, unsafe_allow_html=True)

    with visual3:
        fig = ff.compare_language_columns_and_plot(df, 'LanguageHaveWorkedWith', 'LanguageDesireNextYear')
        st.plotly_chart(fig)
    
    with analysis3:
        language_text = """
        <div class='analysis-container'>
            <div class='analysis-title'>Analysis: Languages Trend</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                 A lot of languages have been presented before us. Many of which seem to be still popular amongst developers.
                StackOverflow asked what language they work with, and want to work with. Many users want to work with the same language they have worked with.
                <br>However, if we look at the big picture, some of the languages are more popular than others. JavaScript, HTML/CSS, Python are leading the market.

        </div>
    """
        st.markdown(language_text, unsafe_allow_html=True)

    with visual3:
        fig = ff.compare_language_columns_and_plot(df, 'DatabaseHaveWorkedWith', 'DatabaseWantToWorkWith')
        st.plotly_chart(fig)

    with analysis3:
        database_base = """
        <div class='analysis-container'>
            <div class='analysis-title'>Analysis: Database Trend</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                A lot of databases have been presented before us. Many of which seem to be still popular amongst developers.
                StackOverflow asked what databases they work with, and want to work with. Many users want to work with the same Database they have worked with.
                <br>However, if we look at the big picture, almost all of the databases are similarly popular, with MySQL and postgresSQL leading.
        </div>
    """
        st.markdown(database_base, unsafe_allow_html=True)

    with visual3:
        fig = ff.compare_language_columns_and_plot(df, 'WebframeHaveWorkedWith', 'WebframeWantToWorkWith')
        st.plotly_chart(fig)

    with analysis3:
        webframe_text = """
        <div class='analysis-container'>
            <div class='analysis-title'>Analysis: Webframes Trends</div>
            <div class='analysis-text' style="color: red; font-weight: bold;">
                 A lot of frameworks have been presented before us. Many of which seem to be still popular amongst developers.
                StackOverflow asked what framework they work with, and want to work with. Many users want to work with the same framework they have worked with.
                <br>However, if we look at the big picture, some of the frameworks are more popular than others. ReactJS, Express are clearly leading the market.
        </div>
    """
        st.markdown(webframe_text, unsafe_allow_html=True)

