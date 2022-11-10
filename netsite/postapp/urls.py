
from django.urls import path
from . import views

app_name = "postapp"

urlpatterns = [    
  path("", views.post), 
  path('postapp/', views.post),
]