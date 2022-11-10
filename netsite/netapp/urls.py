# netapp/urls.py

from django.urls import path
from . import views

app_name = "netapp"

urlpatterns = [
  path("", views.index),
  path('netapp/', views.index),
]