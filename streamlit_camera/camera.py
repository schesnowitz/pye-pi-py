import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    cam_image = st.camera_input("cam")

if cam_image:
    image = Image.open(cam_image)
    gray_image = image.convert('L')
    st.image(gray_image)
