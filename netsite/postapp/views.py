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

month = '2022-11-12'
column_list = ['Region', 'Carbon']
state_carbon = '../static/data/carbon_data_real.csv'
df = pd.read_csv(state_carbon, encoding='euc-kr')
df.columns = column_list

state_geo = '../static/data/TL_SCCO_SIG_WGS84.json'
json_data = open(state_geo, encoding='utf-8').read()
json_Result = json.loads(json_data)

dictionary = {'code': ['11', '26', '27', '28', '29', '30', '31', '41', '42',
              '43', '44', '45', '46', '47', '48', '50', '36']}

region_data = pd.DataFrame(data=dictionary)

bins = [0, 460017, 1228571, 1975424, 2677516, 2853723, 3591552, 12000000]
m = folium.Map(location=[36, 127], zoom_start=7)
m.choropleth(
  geo_data=json_data,
  name='Carbon',
  data=region_data,
  columns=['code', 'data'],
  key_on='feature.properties.CTPRVN_CD',
  fill_color='Blues',
  fill_opacity=0.7,
  line_opacity=0.3,
  color='gray',
  bins=bins
)

folium.LayerControl().add_to(m)
m.save(month + '.html')