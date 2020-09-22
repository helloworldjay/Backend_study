from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail), # pk가 int로 넘어온다.
    # re_path(r'(?P<pk>\d+)/$', views.post_detail) 위의 path와 같은 역할이지만 문자열로 pk가 넘어온다.
    # '<int..>' 이 부분을 Converter라고 부른다
]