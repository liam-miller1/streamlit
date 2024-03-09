import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from folium import plugins

st.set_page_config(page_title="User Input", layout="wide")
st.title('User Input')

political_countries_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson")

m = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron",control_scale=True)

# use Geopandas to buffer input
file = gpd.read_file("Portland_City_Council_Districts.shp")
file["buffered"] = file.buffer(10000)
df2 = file.set_geometry("buffered")

# add to folium map and set the geometry column
folium.GeoJson(df2["buffered"]).add_to(m)

## Add layer control
folium.LayerControl(collapsed=False).add_to(m)

# Fullscreen toggle
plugins.Fullscreen(
    position='topright',
    title='Expand me',
    title_cancel='Exit me',
    force_separate_button=True
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=1500,returned_objects=[])
