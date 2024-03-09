import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from folium import plugins

st.set_page_config(page_title="User Input", layout="wide")
st.title('User Set Buffer')
st.subheader('Map refreshes after number added')


m = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron",control_scale=True)

# create input number box and show it running live on page
number = st.number_input('Insert a number')
st.write('The current number is ', number)

# use Geopandas to buffer input
file = gpd.read_file("Portland_City_Council_Districts.shp")
file["buffered"] = file.buffer(number)
df2 = file.set_geometry("buffered")

# add to folium map and set the geometry column
folium.GeoJson(df2["buffered"]).add_to(m)

## Add layer control
folium.LayerControl(collapsed=False).add_to(m)



# call to render Folium map in Streamlit
st_data = st_folium(m,width=1750, height=500)
