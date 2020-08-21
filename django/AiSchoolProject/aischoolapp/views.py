from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

students = ['광개토대왕', '홍길동', '세종대왕']

def home(request):
    chat = "Hello"
    name = "Jay!"
    return render(request, "home.html", {'user_chat': chat, 'user_name': name})

def login(request):
    return HttpResponse("u got logged in!")

def signout(request):
    return HttpResponse("u got signed out!")

def result(request):
    name = request.POST['username']

    if name in students:
        is_exist = True
    else:
        is_exist = False
    return render(request, "result.html", {'user_name': name, 'is_exist': is_exist})