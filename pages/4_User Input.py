import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="User Input")
st.title('User Input')


# create input text box and show it running live on page
text_input1 = st.text_input("input 1")
st.markdown("Text entered is equal to: " + text_input1)