from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'app/index.html')


def basics(request):
    context = {
        "name" : "코난",
        "job" : "탐정",
        "height" : 150,
        "hobby" : ["추리하기", "사건 만들기", "희생자 만들기"],
        "today" : datetime.now(),
        "users" : [
            {"id" : 1, "name" : "뭉치", "study" : False},
            {"id" : 2, "name" : "세모", "study" : False},
            {"id" : 3, "name" : "아름", "study" : True},
        ],
        "users" : [],
        "eng_name" : "conan",
        "price" : 1254.698
    }
    return render(request, 'app/01_basics.html', context)

def layout(request):
    return render(request, 'app/02_layout.html')

def staticfiles(request):
    return render(request, 'app/03_staticfiles.html')

def urls(request):
    return render(request, 'app/04_urls.html')

def product(request, id):
    print('@@@@@product id  [path variable]@@@@@')
    return render(request, 'app/04_urls.html')

def search(request):
    print(request.GET)
    # q = request.GET.get('q')
    # lang = request.GET.get('lang')
    # return render(request, 'app/04_urls.html', {'q' : q, 'lang' : lang})
    return render(request, 'app/04_urls.html')