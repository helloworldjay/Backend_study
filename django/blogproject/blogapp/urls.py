
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "blogapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('fbv/', views.fbv, name='fbv'),
    path('cbv/', views.cbv, name='cbv'),
]
