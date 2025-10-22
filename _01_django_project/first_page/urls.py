from django.urls import path
from first_page import views

app_name = 'first'

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
]