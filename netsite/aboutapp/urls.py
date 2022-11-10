from django.urls import path
from . import views

app_name = "aboutapp"

urlpatterns = [    
  path("", views.about), 
  path('aboutapp/', views.about),
]