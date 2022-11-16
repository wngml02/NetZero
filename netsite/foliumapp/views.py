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
  
        state_geo = "foliumapp/skorea-provinces-2018-topo-simple.json"
        geo_data = json.load(open(state_geo, encoding='utf-8'))

        df = pd.read_csv('foliumapp/Si_Do.csv', encoding='utf-8')
        m = folium.Map(location=[36.45, 127.42], zoom_start=5)
        m.choropleth(
            geo_data = df,
            name='choropleth',
            data=df,
            columns=['State','Unemployment'],
            key_on = 'feature.properties.name_eng',
            fill_color = 'YlGn',
            fill_opacity=0.7,
            legent_name='Rate'
        )
        folium.LayerControl().add_to(m)
        m.save('./foliummm.html')

def foliumm(request):
  show_map()
  return render(request, '../templates/foliummm.html')
