import streamlit as st
import plotly.express as px

st.title("Five Day Forcaster")
city = st.text_input(placeholder="Enter a city", label="city").title()

days = st.slider("days_slider", min_value=1, max_value=5,
                 help="Select the number of days")
option = st.selectbox("Select data", ("Temerature", "Sky"))
st.subheader(f"{option} for the next {days} in {city}")


def get_data(days):
    dates = ["2012", "2014", "2017"]
    temperature = [23, 21, 5]
    temperature = [days * i for i in temperature]
    return dates, temperature

d, t = get_data()

figure = px.line(x=d, y=t, labels={"x": "Date",
                    "y": "Temperature (C)"})

st.plotly_chart(figure)

