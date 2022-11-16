from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from views import *
import users.views
from django.contrib.auth import login as auth_login

urlpatterns = [
    path('users/', include('users.urls')),
] 

app_name = "users"
urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path("", views.login), 
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('signup/', users.views.signup, name='signup'),
]
