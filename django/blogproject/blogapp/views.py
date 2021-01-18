from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html', {})

def fbv(request):
    return render(request, 'blogapp/fbvbase.html',{})

def cbv(request):
    return render(request, "blogapp/cbvbase.html", {})