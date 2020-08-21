from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html")

def login(request):
    return HttpResponse("u got logged in!")

def signout(request):
    return HttpResponse("u got signed out!")