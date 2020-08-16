from django.shortcuts import render
from books.models import books_to_read
# Create your views here.

def books_index(request):
    books = books_to_read.objects.all()
    context = {
        "books": books
    }
    return render(request,'books_index.html',context)

def book_detail(request,pk):
    book = books_to_read.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request,'book_detail.html',context)