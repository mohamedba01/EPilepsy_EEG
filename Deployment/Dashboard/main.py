
from multiapp import MultiApp
import streamlit as st
import sentiment
import prediction

st.set_page_config(layout="wide")
from PIL import Image
logo = Image.open('logo.png')
st.sidebar.image(logo)

PAGES = {
    "Sentiment Analysis Dashboard": sentiment,
    "Seizure Dectection Dashboard": prediction
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]

page.app()