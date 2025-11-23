
# Import the generic views from Django REST Framework
from rest_framework import generics
# Import viewsets for handling full CRUD operations
from rest_framework import viewsets
# Import our Book model
from .models import Book
# Import our BookSerializer
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API view that returns a list of all books in the database.
    
    This view handles GET requests to retrieve all Book objects.
    The ListAPIView automatically:
    - Fetches all books from the database
    - Serializes them using BookSerializer
    - Returns them as JSON in the response
    
    URL: /api/books/
    """
    
    # queryset: Defines which objects to retrieve from the database
    # Book.objects.all() gets ALL books from the database
    queryset = Book.objects.all()
    
    # serializer_class: Specifies which serializer to use
    # This will convert Book objects into JSON format
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing ALL CRUD operations on Book objects.
    
    This single class handles ALL of these operations automatically:
    - LIST (GET /api/books_all/) - Get all books
    - CREATE (POST /api/books_all/) - Create a new book
    - RETRIEVE (GET /api/books_all/1/) - Get a specific book by ID
    - UPDATE (PUT /api/books_all/1/) - Update a specific book completely
    - PARTIAL UPDATE (PATCH /api/books_all/1/) - Update specific fields
    - DESTROY (DELETE /api/books_all/1/) - Delete a specific book
    
    ModelViewSet provides all these methods out of the box!
    You don't have to write separate views for each operation.
    """
    
    # Define which objects this ViewSet will work with
    queryset = Book.objects.all()
    
    # Define which serializer to use for converting data
    serializer_class = BookSerializer








