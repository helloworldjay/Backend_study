from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    chat = "Hello"
    name = "Jay!"
    return render(request, "home.html", {'user_chat': chat, 'user_name': name})

def login(request):
    return HttpResponse("u got logged in!")

def signout(request):
    return HttpResponse("u got signed out!")