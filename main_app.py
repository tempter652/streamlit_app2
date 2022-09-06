import streamlit as st
from PIL import Image

st.title('テストアプリ')
st.caption('これは,streamlitのテストアプリです.')

# 画像
image = Image.open('./data/ureshi.jpg')
st.image(image, width=200)
