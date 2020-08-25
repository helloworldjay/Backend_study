from django.shortcuts import render

students = ['세종대왕', '광개토대왕']

# Create your views here.
def home(request):
    chat = "hi there"
    name = "Jay"
    context = {'chat' : chat, 'name' : name}
    return render(request, 'home.html', context)


def result(request):
    name = request.POST['username']
    
    if name in students :
        is_exist = True
    else :
        is_exist = False
    
    context = {'name' : name, 'is_exist' : is_exist}

    return render(request, 'result.html', context)