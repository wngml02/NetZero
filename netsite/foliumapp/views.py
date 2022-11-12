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



def mapping():
  csvFile = 'Si_Do_Carbon_ratio.csv'
  SiDodf = pd.read_csv(csvFile, encoding='utf-8')
    
  geo_data = json.load(open('Si_Do_map_utf8.json', encoding='utf-8'))
  df_adm = SiDodf.groupby(['Region'])['Carbon'].sum().to_frame().reset_index()
  
  m = folium.Map(location=[36.45,127.42], titles="OpenStreetMap", zoom_start=8)
  

  folium.Choropleth(
    geo_data = geo_data,
    name = '탄소배출량',
    data = df_adm,
    columns = ["Region", 'Carbon'],
    key_on = 'feature.properties.Region',
    fill_color ='PuRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='탄소배출량',
  ).add_to(m)
    
  folium.LayerControl().add_to(m)
  return m.save('../foliumapp/templates/foliumapp/folium_kr.html')

def foliumm(request):
  return render(request, './foliumapp/folium_kr.html')
