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
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
      auth.login(request, user)
      return redirect('/')
  else:
    return render(request, 'users/login.html', {'error': 'username or password is incorrect'})
  return render(request, 'users/login.html')

@csrf_exempt
def search(request):
  return HttpResponse('success')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            auth.login(request,user)  # type: ignore # 로그인
            return redirect('/')
    else:
      form = UserForm()
      return render(request, 'users/signup.html', {'form': form})

""" def signup(request):
    if request.method == 'POST':
      if request.POST['password'] == request.POST['password']:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        auth.login(request, user)
        return redirect('/')
    return render(request, 'users/signup.html') """

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    return redirect('/')
  return render(request,'netapp/index.html')