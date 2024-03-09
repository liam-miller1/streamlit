import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from folium import plugins

st.set_page_config(page_title="User Input", layout="wide")
st.title('File Uploader')

file = st.file_uploader(label='label')

if file is not None:

    #To read file as bytes:

    #bytes_data = file.getvalue()

    #st.write(bytes_data)
    
    st.write(file)



