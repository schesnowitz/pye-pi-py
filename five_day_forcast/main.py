import streamlit as st
import plotly.express as px
from backend import get_weather_data

st.title("Five Day Forcaster")
city = st.text_input(placeholder="Enter a city", label="city").title()

days = st.slider("days_slider", min_value=1, max_value=5,
                 help="Select the number of days")
option = st.selectbox("Select data", ("Temperature", "Sky"))

if days == 1:
    st.subheader(f"{option} for the next day in {city}")
else:
    st.subheader(f"{option} for the next {days} days in {city}")

if city:
    try:
        filtered_data = get_weather_data(city, days)
        if option == "Temperature":
            temperatures = [dict['main']['temp'] / 10 for dict in
                            filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date",
                                     "y": "Temperature (Celsius)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}

            sky_conditions = [dict['weather'][0]['main'] for dict in
                              filtered_data]
            image_paths = [images[condition] for condition in
                           sky_conditions]
            # print(sky_conditions)
            st.image(image_paths, width=100)
    except KeyError:
        st.error(
                "There is a problem with the city name, "
                "please try another city.")
