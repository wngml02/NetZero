from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('users/', include('users.urls')),
] 

app_name = "users"
urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='/users/login.html'), name="login"),
  path("", views.login), 
  path('logout/',auth_views.LogoutView.as_view(next_page="/posttwoapp/"),name='logout'),
]

urlpatterns = [
    path('home/signup/', signup, name='signup'),
]