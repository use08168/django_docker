from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello i'm index</h1>")

def hello(request):
    print('hello 함수 호출')
    return HttpResponse('<h1>Hello Django</h1>')

