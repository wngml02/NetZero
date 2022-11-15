from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from views import *
import users.views

urlpatterns = [
    path('users/', include('users.urls')),
] 

app_name = "users"
urlpatterns = [
  path('login/', users.views.login, name="login"),
  path("", views.login), 
  path('logout/', users.views.logout, name='logout'),
  path('signup/', users.views.signup, name='signup'),
]
