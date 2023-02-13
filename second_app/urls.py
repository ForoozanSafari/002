from django.urls import path
from django.shortcuts import render

def login(request):
    return render(request,'second_app\login ')# 
