from django.shortcuts import render

# Create your views here.
def posttwo(request):
  return render(request, 'posttwoapp/post2.html')

def my_view(request):
  if request.method == 'POST':
    checksave = request.POST.getlist('checksave')
    print(checksave)
  return render(request, 'post2.html')

def input_test(request):
  if request.POST:
    list_item = request.POST.getlist('test')
    print(list_item)
    
