import streamlit as st
import pandas as pd

data = pd.read_csv("data.csv", sep=";")

# print(data)

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    selfie = st.image("images/1.png")

with col2:
    st.title("Stephen Chesnowitz")
    content = """
    Lorem Ipsum is simply dummy text of the printing 
    and typesetting industry. Lorem Ipsum has been the industry's 
    standard dummy text ever since the 1500s, when an unknown 
    printer took a galley of type and scrambled it to make a type 
    specimen book. It has survived not only five centuries, 
    but also the leap into electronic typesetting, remaining 
    essentially unchanged. It was popularised in the 1960s with the 
    release of Letraset sheets containing Lorem Ipsum passages, 
    and more recently with desktop publishing software like Aldus 
    PageMaker including versions of Lorem Ipsum.
    """
    st.info(content)
content2 = """
Below are some python apps I have built.
"""
st.text(content2)
# title;description;url;image
col3, col4 = st.columns(2)

with col3:
    for i, row in data[0:10].iterrows():
        st.header(row['title'])

with col4:
    for i, row in data[10:].iterrows():
        st.header(row['title'])
