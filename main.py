import streamlit as st
from PIL import Image, ImageOps

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

image = Image.open('images/IMG_4626.JPG')
image = ImageOps.exif_transpose(image) #ImageOps.exif_transpose(image) reads the EXIF orientation tag (e.g., rotate 90°, flip, etc.) and transforms the image accordingly.

with col1:
    st.image(image, caption='Me with my Heart in hand')

with col2:
    st.text("Soham Roy")
    content = """ I am a DevOps Engineer. To be better at my job I have now taken up the challenge to learn Python and Java"""
    st.info(content)


