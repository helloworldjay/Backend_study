from django.shortcuts import render
from django.http import HttpResponse
from .models import AiClass

# Create your views here.

# def home(request):
#     name = 'Jay'
#     student_num = 1


#     context = {
#         'name' : name,
#         'student_num' : student_num
#     }
    
#     return render(request, 'home.html', context)

def home(request):
    class_object = AiClass.objects.all()
    return render(request, 'home.html', {'class_object':class_object})


name_list = ['폰노이만', '앨런 튜링']

def result(request):
    name = request.POST['username']
    if name in name_list:
        is_exist = True
    else:
        is_exist = False
    context = {
        'user_name' : name,
        'is_exist' : is_exist
    }
    
    return render(request, 'result.html', context) 