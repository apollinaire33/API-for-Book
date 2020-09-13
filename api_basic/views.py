from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Book
from .serializers import BookListSerializer, BookDetailSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def book_list(request):
    
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many = True)  
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookDetailSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)


@csrf_exempt
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BookDetailSerializer(book)
        return JsonResponse(serializer.data)
    
    elif request.method == 'DELETE':
        book.delete()
        return HttpResponse(status=204)
