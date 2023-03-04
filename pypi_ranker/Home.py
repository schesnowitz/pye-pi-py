import streamlit as st
import pandas as pd
import time


def column_data():
    image_location = 'images/' + row['image_src']
    stats = (f"At position {row['column_index']} "
             f"with {row['downloads']} downloads")
    url = f"[PyPI Stats]({row['py_url']})"
    st.image(image_location)
    st.markdown(
        f'<h2 style="color: teal;">#{row["column_index"]} {row["package"]}</h2>',
        unsafe_allow_html=True)
    st.markdown(f'<i style="color: blue;">{stats}</i>',
                unsafe_allow_html=True)
    st.write(row["description"])
    st.write(url)


# END column_data()==================================================

st.set_page_config(layout="wide")
data = pd.read_csv("data.csv", sep=",")
date = (time.strftime(f"%B 1st, %Y"))
# col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
st.title("The Pypi Ranker")
st.subheader(f"The top 20 downloaded python packages as of {date}")
st.caption(
    ':red[ Coming soon with weekly trends! 😉]')

top_col1, spacer_col, top_col2 = st.columns([1.5, 0.5, 1.5])

with top_col1:
    for index, row in data[0:1].iterrows():
        column_data()

with top_col2:
    for index, row in data[1:2].iterrows():
        column_data()

right_col, content_col, left_col = st.columns([1.0, 2, 1.0])

with content_col:
    st.subheader("The rest of the pack...")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in data[2:8].iterrows():
        column_data()

with col2:
    for index, row in data[8:14].iterrows():
        column_data()

with col3:
    for index, row in data[14:20].iterrows():
        column_data()
