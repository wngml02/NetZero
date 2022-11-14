from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.forms import UserForm

# Create your views here.
def login(request):
  return render(request, 'users/login.html')

@csrf_exempt
def search(request):
  return HttpResponse('success')

def signup(request):
    if request.method == 'POST':
      form = UserForm(request.POST)
      if form.is_valid():
        form.save()
        username= form.cleaned_data.get['username']
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username,password=raw_password)
        login(request, user)
        return redirect('posttwo')
      else:
        form = UserForm()
      return render(request, 'users/signup.html', {'form':form})