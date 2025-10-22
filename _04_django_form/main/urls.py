from django.urls import path
from main import views
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

app_name = 'main'

urlpatterns=[
    path('contact/', views.contact_view, name='contact'),
    path('book/', views.create_book_view, name='book'),
    path('upload/', views.upload_view, name='upload'),

    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('books/create', BookCreateView.as_view(), name='book_create'),
    path('books/update', BookUpdateView.as_view(), name='book_update'),
    path('books/delete', BookDeleteView.as_view(), name='book_delete'),
]

