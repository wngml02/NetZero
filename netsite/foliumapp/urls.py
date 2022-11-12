
from django.urls import path
from . import views

app_name = "foliumapp"

urlpatterns = [    
  path("", views.foliumm), 
  path('foliumapp/', views.foliumm),

]