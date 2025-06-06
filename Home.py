import streamlit as st
from PIL import Image, ImageOps
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns([1.5, 2])

image = Image.open('images/IMG_4626.JPG')
image = ImageOps.exif_transpose(image) #ImageOps.exif_transpose(image) reads the EXIF orientation tag (e.g., rotate 90°, flip, etc.) and transforms the image accordingly.

with col1:
    st.image(image, caption='Me with my Heart in hand', use_container_width =True) # width=600) # or use_container_width =True)

with col2:
    st.header("Soham Roy")
    content = """ I am a DevOps Engineer. To be better at my job I have now taken up the challenge to learn Python and Java"""
    st.subheader(content)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

dt = pandas.read_csv('data.csv', sep=";")

with col3:
    for index, row in dt[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("./images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in dt[10:].iterrows():
        st.header(row["title"])
        st.write(f"[Source Code]({row['url']})")
        st.image("./images/" + row["image"])

