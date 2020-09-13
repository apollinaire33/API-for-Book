from rest_framework import serializers
from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name'] 


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author_name', 'description'] 



    
    