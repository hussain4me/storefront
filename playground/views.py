from django.shortcuts import render
# from django..htpp import HttpResponse

# Create your views here.

def say_hello(request):
    # return HttpResponse('Hello, world')
    return render(request,'hello.html', {'name':'Hussain'})