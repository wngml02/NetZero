from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
def login(request):
  return render(request, 'users/login.html')

@csrf_exempt
def search(request):
  return HttpResponse('success')