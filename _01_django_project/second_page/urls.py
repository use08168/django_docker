from django.urls import path
from second_page import views

app_name = 'second'

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
]