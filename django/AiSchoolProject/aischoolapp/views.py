from django.shortcuts import render
from django.http import HttpResponse
from .models import AiClass, AiStudents
# Create your views here.

students = ['광개토대왕', '홍길동', '세종대왕']

def home(request):
    class_object = AiClass.objects.all()
    context = {'class_object': class_object}
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


def detail(request, class_pk):
    print(class_pk)

    class_obj = AiClass.objects.get(pk=class_pk)
    student_obj = AiStudents.objects.filter(class_num=class_pk)

    context = {
        'class_pk': class_pk,
        'class_obj' : class_obj,
        'student_obj' : student_obj
    }
    return render(request, 'detail.html', context)

def add(request, class_pk):

    class_obj = AiClass.objects.get(pk=class_pk)

    if request.method == 'POST' :
        AiStudents.objects.create(
            class_num = class_pk,
            name = request.POST['name'],
            phone_num=request.POST['phone_num'],
            intro_text=request.POST['intro_text']
        )
        return redirect('detail', class_pk)

    context = {
        'class_obj': class_obj
    }
    return render(request, 'add.html', context)