from django.urls import path, include
from .views import book_list, book_detail


urlpatterns = [
    path('books/', book_list),
    path('books/<int:pk>/', book_detail),
]