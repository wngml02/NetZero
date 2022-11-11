from django.shortcuts import render
import requests
import json
import pandas as pd
import csv
import numpy as np
from pandas.io.json import json_normalize
import os
import webbrowser
import folium
from folium import plugins


# Create your views here.
def post(request):
  return render(request, 'postapp/post.html')

state_geo = './postapp/TL_SCCO_SIG_WGS84.json'

state_carbon = './postapp/static/data/carbon_data_real.csv'
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
  fill_color='Blues',
  fill_opacity=0.7,
  line_opacity=0.3,
  color='gray',
  legend_name='carbon'
)

folium.LayerControl().add_to(m)

# Save to html
m.save('folium_kr.html')
webbrowser.open_new("folium_kr.html")

json_data = open(state_geo).read()
jsonResult = json.loads(json_data)

# 중앙위치 계산
def center_calc(points_df):
  x = points_df.x
  y = points_df.y

  X = (max(x)+min(x))/2
  Y = (max(y)+min(y))/2

  return x,y

# 다중 Array 구조 이중으로 변환
def points_array(points):
  final_points = []

  for x in range(0, len(points)):
    if len(points[x]) == 2:
      final_points.append(points[x])
    else:
      target = points[x]
      for y in range(0, len(target)):
        final_points.append(target[y])

  return final_points

# 구역별 중심 DataFrame 생성
center_locations = pd.DataFrame()
codes = []
names = []
x_list = []
y_list = []
for x in range(0, len(jsonResult['features'])):
  code = jsonResult['features'][x]['properties']['SIG_CD']
  name = jsonResult['features'][x]['properties']['SIG_KOR_NM']
  # 중앙값 생성
  points = jsonResult['features'][x]['geometry']['coordinates'][0]
  points = points_array(points)
  points_df = pd.DataFrame(points)
  points_df.columns = ['x','y']
  X, Y = center_calc(points_df)

# 결과
  codes.append(code)
  names.append(name)
  x_list.append(X)
  y_list.append(Y)

# 데이터프레임 생성
center_locations['CODE'] = codes
center_locations['NAME'] = names
center_locations['X'] = x_list
center_locations['Y'] = y_list  

target_df = pd.merge(state_data,center_locations, how = 'left', on = 'Region')
target_df = target_df[~np.isnan(target_df['X'])] # 위치 정보 없는 값 제외