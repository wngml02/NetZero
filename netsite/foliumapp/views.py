from django.shortcuts import render

# Create your views here.
def foliumm(request):
  return render(request, 'foliumapp/folium_kr.html')