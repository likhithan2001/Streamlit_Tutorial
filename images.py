import streamlit as st
from PIL import Image

image = Image.open('Liki.jpg')
st.image(image,caption="Nice Picture")