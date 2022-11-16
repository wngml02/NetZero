from django.urls import path
from . import views

app_name = "calcapp"

urlpatterns = [    
  path("", views.result), 
  path('calcapp/', views.result),
]