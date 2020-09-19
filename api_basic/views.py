from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from .models import Book
from .serializers import BookListSerializer, BookDetailSerializer
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

@csrf_exempt
def book_list(request):
    
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many = True)  
        return render(request, 'books/list.html', {'books': books})
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
        return render(request, 'books/detail.html', {'book': book})
        return JsonResponse(serializer.data)
    
    elif request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
        return HttpResponseRedirect( reverse('books:book_list') )

@csrf_exempt
def book_add(request):   
    if request.method == 'GET':
        book = Book.objects.all()
        return render(request, 'books/adding.html', {'book': book})
        
    elif request.method == 'POST':
        book = Book.objects.all()
        book.create(title = request.POST['title'], author_name = request.POST['author'], description = request.POST['description'], image = request.POST['image'])
        return HttpResponseRedirect( reverse('books:book_list') )
