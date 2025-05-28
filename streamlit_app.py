import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder()

countries = sorted(df['country'].unique().tolist())

st.title("Global Development Dashboard")
st.sidebar.markdown("""Explore global trends in **GDP per capita** using the Gapminder dataset.
Select a country below to view its data. Default is *Canada*.""")

country_selected = st.sidebar.selectbox(
    "Select a country:",
    countries,
    index=countries.index("Canada")
)
st.markdown(
    "Dataset includes GDP per capita, life expectancy, and population for 142 countries over time.")
st.dataframe(df.head())


# Filter the country based on the user's selection
# Show only the row that matches the selected country
filtered_df = df[df['country'] == country_selected]

st.subheader(f"{country_selected} GDP per Capita Over Time")
line = px.line(filtered_df, x='year', y='gdpPercap', markers=True,
               title="GDP per Capita Growth")
st.plotly_chart(line)


year_selected = st.sidebar.slider(
    "Select year for global comparison:",
    min_value=int(df['year'].min()),
    max_value=int(df['year'].max()),
    value=2007,
    step=5,
)

year_df = df[df['year'] == year_selected]

scatter = px.scatter(year_df, x='gdpPercap', y='lifeExp', size='pop', color='continent',
                     hover_name='country',
                     log_x=True, title=f"GDP per Capita vs Life Expectancy ({year_selected})")
st.plotly_chart(scatter)