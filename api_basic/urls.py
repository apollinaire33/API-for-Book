from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'books'
urlpatterns = [
    path('books/', views.book_list, name = 'book_list'),
    path('books/<int:pk>/', views.book_detail, name = 'book_detail'),
    path('books/adding/', views.book_add, name = 'book_add'),
]