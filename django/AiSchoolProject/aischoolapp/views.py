from django.shortcuts import render
from django.http import HttpResponse
from .models import AiClass
# Create your views here.

students = ['광개토대왕', '홍길동', '세종대왕']

def home(request):
    classes = AiClass.objects.all()
    context = {'class object': classes}
    return render(request, "home.html", context)

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


