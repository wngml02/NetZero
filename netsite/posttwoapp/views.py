from django.shortcuts import render

# Create your views here.
def posttwo(request):
  return render(request, 'posttwoapp/post2.html')

def my_view(request):
  if request.method == 'POST':
    eat1 = request.POST.getlist('eat1')
    print(eat1)
  return render(request, 'post2.html')