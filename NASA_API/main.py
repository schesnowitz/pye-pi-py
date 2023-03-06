import streamlit as st
import requests
import os

nasa_key = os.getenv('NASA_API')

url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_key}'
request = requests.get(url)
# data as dict
response = request.json()

image_url = response["hdurl"]
img_response = requests.get(image_url)
print(img_response.content)
# with open("image.jpg", 'wb') as file:
#     file.write(img_response.content)
# print(content["hdurl"])
st.title(response["title"])
st.image(img_response.content, caption=None, width=None,
         use_column_width=None, clamp=False, channels="RGB",
         output_format="auto")
st.write(response["explanation"])
st.write(response)