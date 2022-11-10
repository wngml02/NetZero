from django.urls import path
from . import views

app_name = "posttwoapp"

urlpatterns = [    
  path("", views.posttwo), 
  path('posttwoapp/', views.posttwo),
]