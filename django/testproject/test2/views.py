from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    context= { 'name' : 'hello world'}
    return HttpResponse("{ 'name' : 'hello world'}")