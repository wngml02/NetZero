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
        state_geo = "foliumapp/Si_Do.json"
        state_unemployment = 'foliumapp/Si_Do.csv'
        state_data = pd.read_csv(state_unemployment)
        m = folium.Map(location=[36.45, 127.42], zoom_start=5)
        m.choropleth(
            geo_data = state_geo,
            name='choropleth',
            data=state_data,
            columns=['State','Unemployment'],
            key_on = 'feature.id',
            fill_color = 'YlGn',
            fill_opacity=0.7,
            line_opacity=0.2,
            legent_name='Rate (%)'
        )
        folium.LayerControl().add_to(m)
        m.save('foliumapp/templates/foliumapp/foliummm.html')

def foliumm(request):
  show_map()
  return render(request, 'foliumapp/foliummm.html')
