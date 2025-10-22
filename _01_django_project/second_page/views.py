from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    #return HttpResponse("<h1>This is Second Index Page 히히</h1>")
    return render(request, 'second/index.html')

def hello(request):
    print('hello 함수 호출')
    return HttpResponse('<h1>Hello Django</h1>')

