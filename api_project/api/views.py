from django.shortcuts import render


from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API view that returns a list of all books in the database.
    
    This view handles GET requests to retrieve all Book objects.
    The ListAPIView automatically:
    - Fetches all books from the database
    - Serializes them using BookSerializer
    - Returns them as JSON in the response
    """
    
    # queryset: Defines which objects to retrieve from the database
    # Book.objects.all() gets ALL books from the database
    queryset = Book.objects.all()
    
    # serializer_class: Specifies which serializer to use
    # This will convert Book objects into JSON format
    serializer_class = BookSerializer






