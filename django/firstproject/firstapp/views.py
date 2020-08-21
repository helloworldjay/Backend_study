from django.shortcuts import render
from django.http import HttpResponse


def helloworld(request):
    return HttpResponse('Hello World!')

def login(request):
    return HttpResponse('login!')

def signout(request):
    return HttpResponse('signout')


# Create your views here.
