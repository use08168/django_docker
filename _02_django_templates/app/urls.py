from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('basics/', views.basics, name='basics'),
    path('layout/', views.layout, name='layout'),
    path('staticfiles/', views.staticfiles, name='staticfiles'),
    path('urls/', views.urls, name='urls'),
    path('product/<int:id>', views.product, name='product'),
    path('search/', views.search, name='search'),
]