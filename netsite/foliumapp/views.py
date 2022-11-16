from django.shortcuts import render
import csv
import json
import os
import webbrowser

import folium
import numpy as np
import pandas as pd
import requests
from django.shortcuts import render
from folium import plugins
from pandas.io.json import json_normalize
from folium.plugins import HeatMap
  
def show_map():
  csvFile = 'foliumapp/Si_do.csv'
  SiDodf = pd.read_csv(csvFile, encoding='utf-8')
  jsonFile = 'foliumapp/Sidojson.json'
  Sido_geo = json.load(open(jsonFile, encoding='utf-8'))
  
  m=folium.Map(location=[36.45,127.42],title="OpenStreetMap",zoom_start=8)
  folium.Choropleth(
    geo_data=Sido_geo,
    name="carbonmap",
    data=SiDodf,
    columns=['Sido','carbon'],
    key_on='feature.properties.CTP_ENG_NM',
    fill_color='PuRd',
    fill_opacity=0.7,
    legend_name='carbonmap').add_to(m)
  folium.LayerControl().add_to(m)
  
  m.save('foliumapp/map.html')
  webbrowser.open('foliumapp/map.html')

def foliumm(request):
  show_map()
  return render(request, 'foliumapp/map.html')
