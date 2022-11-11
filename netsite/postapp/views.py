from django.shortcuts import render
import requests
import json
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import os
import webbrowser
import folium
from folium import plugins


# Create your views here.
def post(request):
  return render(request, 'postapp/post.html')

state_geo = 'TL_SCCO_SIG_WGS84.json'

state_carbon = './carbon_data_real.csv'
state_data = pd.read_csv(state_carbon, encoding='EUC-KR')
state_data.columns = ['Region','CO2','CH4','N2O','Total']
state_data.head(1)

# Initialize the map
m = folium.Map(location=[36, 127], titles="OpenStreetMap", zoom_start=7)

m.choropleth(
  geo_data=state_geo,
  name='탄소배출량',
  data=state_data,
  columns=['Region','CO2','CH4','N2O','Total'],
  key_on = 'feature.properties.SIG_CD',
  fill_color='YlGn',
  fill_opacity=0.7,
  line_opacity=0.3,
  color='gray',
  legend_name='carbon'
)

folium.LayerControl().add_to(m)

# Save to html
m.save('folium_kr.html')
webbrowser.open_new("folium_kr.html")
