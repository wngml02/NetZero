from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
  return render(request, 'users/login.html')

@csrf_exempt
def search(request):
  return HttpResponse('success')

def signup(request):
    if request.method == 'POST':
      if request.POST['password1'] == request.POST['password2']:
        user = User.objects.create_user(
          username = request.POST['username'],
          password = request.POST['password1'],
          email = request.POST['email'],
        )
        auth.login(request, user)
        return redirect('/')
      return render(request, 'signup.html')
    return render(request, 'signup.html')
