from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('users/', include('users.urls')),
]

app_name = "users"
urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
  path("", views.login), 
  path('users/', views.login),
]