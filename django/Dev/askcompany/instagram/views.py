from django.views.generic import ListView
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
# Create your views here.

post_list = ListView.as_view(model=Post)

# def post_list(request):
#     qs = Post.objects.all()
#     q= request.GET.get('q','')
#     if q:
#         qs = qs.filter(message__icontains=q)
#         return render(request, 'instagram/post_list.html', {
#             'post_list': qs,
#             'q' :q,
#         })

def post_detail(request : HttpResponse, pk: int) -> HttpResponse: # type을 쓰는 쪽으로 유행이 가고있다
    response = HttpResponse()
    return response

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")