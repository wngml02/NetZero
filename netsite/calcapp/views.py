from django.shortcuts import render,redirect

# Create your views here.

def result(request):
  calc()
  return render(request, 'calcapp/calc.html')

def calc():
  return calc

def eat1(request):
    riceCarbon = 0.5
    rice = int(request.GET.get('rice'))
    context = {
        'rice': rice,
    }
    return rice * riceCarbon