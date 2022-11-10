from django.shortcuts import render

# Create your views here.
def posttwo(request):
  return render(request, 'posttwoapp/post2.html')