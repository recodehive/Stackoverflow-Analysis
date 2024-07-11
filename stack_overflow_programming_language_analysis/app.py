import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
import datetime
import plotly.graph_objects as go
import networkx as nx


# Load and preprocess data using st.cache
st.cache_data(hash_funcs={pd.DataFrame: lambda _: None})
def load_data():
    df = pd.read_csv('TotalQuestions.csv', parse_dates=['Month'])
    df.set_index('Month', inplace=True)
    return df


# Sidebar navigation
menu = st.sidebar.selectbox('Navigation', ['Stack Overflow Question Forecast', 'Graphical Analysis', 'Timeline Visualization'])

if menu == 'Stack Overflow Question Forecast':
    # Load data
    df = load_data()
    languages = df.columns.tolist()


    def forecast_questions(df, language, future_month, future_year):
        model = ARIMA(df[language], order=(5, 1, 0))  # Simple ARIMA model for demonstration
        model_fit = model.fit()
        last_date = df.index[-1]
        future_date = pd.to_datetime(f'{future_year}-{future_month:02d}-01')
        months_ahead = (future_date.year - last_date.year) * 12 + future_date.month - last_date.month
        if months_ahead <= 0:
            raise ValueError("Prediction must have end after start.")
        forecast = model_fit.forecast(steps=months_ahead)
        return forecast.iloc[-1]  # Correctly accessing the last forecasted value


    def generate_forecasts(df, language, start_date, periods):
        model = ARIMA(df[language], order=(5, 1, 0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=periods)
        future_dates = pd.date_range(start=start_date, periods=periods, freq='M')
        forecast_df = pd.DataFrame({language: forecast}, index=future_dates)
        return forecast_df


    # Modify title style
    st.markdown(
        "<h1 style='color: #87CEEB; font-size: 36px;'>Stack Overflow Question Forecast</h1>",
        unsafe_allow_html=True
    )
    st.markdown("---", unsafe_allow_html=True)
    st.subheader('Select Programming Language')
    selected_language = st.selectbox('', languages)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Select Future Month')
        future_month = st.selectbox('', list(range(1, 13)),
                                    format_func=lambda x: datetime.date(1900, x, 1).strftime('%B'))
    with col2:
        st.subheader('Select Future Year')
        future_year = st.selectbox('', list(range(datetime.datetime.now().year, datetime.datetime.now().year + 6)))

    # Forecast for the selected month and year
    if st.button('Predict'):
        try:
            prediction = forecast_questions(df, selected_language, future_month, future_year)
            st.markdown(
                f"<div style='background-color: green; color: white; padding: 10px; border-radius: 5px;'><strong>Predicted number of questions for {selected_language} in {datetime.date(1900, future_month, 1).strftime('%B')} {future_year}: <span style='color: red;'>{int(prediction)}</span></strong></div>",
                unsafe_allow_html=True)

            # Generate additional forecasts for plots
            start_date = df.index[-1] + pd.offsets.MonthBegin()
            forecast_df = generate_forecasts(df, selected_language, start_date, 12)

            # Plot 1: Count plot of total questions for each month in the selected year
            months = pd.date_range(start=f'{future_year}-01-01', end=f'{future_year}-12-31', freq='M')
            month_forecasts = [forecast_questions(df, selected_language, month.month, month.year) for month in months]
            month_forecast_df = pd.DataFrame({selected_language: month_forecasts}, index=months)

            fig1 = px.bar(month_forecast_df, x=month_forecast_df.index.strftime('%B'), y=selected_language,
                          title=f'Monthly Predictions for {future_year}')
            st.plotly_chart(fig1)

            # Plot 2: Sum of total number of questions for the next five years including the predicted year
            future_years = list(range(datetime.datetime.now().year, future_year + 5))
            year_forecasts = []
            for year in future_years:
                if year <= df.index[-1].year:
                    year_forecasts.append(df[df.index.year == year][selected_language].sum())
                else:
                    months = pd.date_range(start=f'{year}-01-01', end=f'{year}-12-31', freq='M')
                    year_forecasts.append(
                        sum([forecast_questions(df, selected_language, month.month, month.year) for month in months]))
            year_forecast_df = pd.DataFrame({selected_language: year_forecasts}, index=future_years)

            fig2 = px.bar(year_forecast_df, x=year_forecast_df.index, y=selected_language,
                          title=f'Yearly Predictions for Next 5 Years for {selected_language}')
            st.plotly_chart(fig2)

            # Plot 3: Pie chart of percentage questions predicted for input year month-wise
            year_forecast_percent = month_forecast_df / month_forecast_df.sum() * 100
            fig3 = px.pie(year_forecast_percent, values=selected_language,
                          names=year_forecast_percent.index.strftime('%B'),
                          title=f'Percentage Question Distribution for {selected_language} in {future_year}')
            st.plotly_chart(fig3)

            # Plot 4: Additional plot as requested (example: line plot for monthly trends)
            fig4 = px.line(month_forecast_df, x=month_forecast_df.index, y=selected_language,
                           title=f'Monthly Trends for {selected_language}')
            fig4.update_traces(mode='lines+markers')
            fig4.update_layout(xaxis_title='Date', yaxis_title='Number of Questions', plot_bgcolor='rgba(0, 0, 0, 0)')
            st.plotly_chart(fig4)

        except ValueError as e:
            st.error(f"Error: {e}")

elif menu == 'Graphical Analysis':

    # Modify title style
    st.markdown(
        "<h1 style='color: #87CEEB; font-size: 36px;'>Graphical Analysis</h1>",
        unsafe_allow_html=True
    )
    st.markdown("---", unsafe_allow_html=True)

    # Load data
    df = load_data()

    # 1) Annual Line Chart
    df_annual = df.resample('A').sum()
    fig1 = px.line(df_annual, x=df_annual.index, y=df_annual.columns,
                   title='Timeline of the number of questions per category (2008-2024)')
    st.plotly_chart(fig1)

    # 2) Change in Question Counts Over Time
    df_change = df.diff()
    fig2 = px.line(df_change, x=df_change.index, y=df_change.columns,
                   title='Change in Question Counts for Each Programming Language Over Time')
    st.plotly_chart(fig2)

    # 4) Total Number of Questions by Programming Languages
    total_questions_by_language = df.sum().sort_values(ascending=False)
    fig4 = px.bar(x=total_questions_by_language.index, y=total_questions_by_language.values,
                  title='Total Number of Questions by Programming Languages')
    st.plotly_chart(fig4)

    # 5) Individual Temporal Series for Top 5 Languages
    top_5_data = df.sum().sort_values(ascending=False).head(5)
    top_5_languages = top_5_data.index.tolist()
    df_top_5 = df[top_5_languages]
    fig5 = px.line(df_top_5, x=df_top_5.index, y=df_top_5.columns,
                   title='Individual Temporal Series for Top 5 Languages')
    st.plotly_chart(fig5)

    # 6) Total Number of Questions by Day of the Week
    daily_total_questions = df.groupby(df.index.dayofweek).sum().sum(axis=1)
    fig6 = px.bar(x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], y=daily_total_questions.values,
                  title='Total Number of Questions by Day of the Week')
    st.plotly_chart(fig6)

    # 7) Heatmap of the Correlation Between Programming Languages
    correlation_matrix = df.corr()
    # Replace 'coolwarm' with a valid Plotly colorscale or a custom colorscale definition
    fig7 = px.imshow(correlation_matrix, color_continuous_scale='thermal',title='Correlation Heatmap of Programming Languages')

    # Display the plot using Streamlit
    st.plotly_chart(fig7)

    # 8) Distribution of Questions for Top 10 Languages
    top_10_data = df.sum().sort_values(ascending=False).head(10)
    top_10_languages = top_10_data.index.tolist()
    df_top_10 = df[top_10_languages]
    fig8 = px.box(df_top_10, y=df_top_10.columns, title='Distribution of Questions for Top 10 Programming Languages')
    st.plotly_chart(fig8)

    # Extract top 10 languages by total questions
    top_10_data = df.sum().sort_values(ascending=False).head(10)
    top_10_languages = top_10_data.index.tolist()

    # Filter the DataFrame to include only the top 10 languages
    df_top_10 = df[top_10_languages]

    # Calculate correlation matrix
    corr_matrix = df_top_10.corr()

    # Create a graph from the correlation matrix
    G = nx.from_numpy_array(corr_matrix.values)

    # Plotting the network
    plt.figure(figsize=(12, 8))
    plt.style.use('dark_background')
    pos = nx.spring_layout(G, seed=42)  # positions for all nodes

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=1500, node_color='skyblue', edgecolors='grey')

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color='grey')

    # Draw labels
    nx.draw_networkx_labels(G, pos, labels={i: top_10_languages[i] for i in range(len(top_10_languages))}, font_size=10,
                            font_weight='bold')

    plt.title('Network Plot of Top 10 Programming Languages based on Correlation')
    plt.show()

    # Displaying both graphs sequentially
    import streamlit as st

    # Display Matplotlib graph
    st.pyplot(plt)


elif menu == 'Timeline Visualization':
    if menu == 'Timeline Visualization':
        st.markdown(
            "<h1 style='color: #87CEEB; font-size: 36px;'>Timeline Visualization</h1>",
            unsafe_allow_html=True
        )
        st.markdown("---", unsafe_allow_html=True)

        # JavaScript to attempt autoplay
        autoplay_js = """
        <script>
        document.addEventListener('DOMContentLoaded', function(event) {
            var video = document.getElementById('autoplay-video');
            video.play();
        });
        </script>
        """
        st.markdown(autoplay_js, unsafe_allow_html=True)

        # Display the MP4 video with autoplay and larger size
        video_path = 'stack_overflow.mp4'  # Replace with your actual video file path
        video_bytes = open(video_path, 'rb').read()
        st.video(video_bytes, start_time=0)