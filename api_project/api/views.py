# Import the generic views from Django REST Framework
from rest_framework import generics
# Import viewsets for handling full CRUD operations
from rest_framework import viewsets
# Import permissions to control access
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
# Import our Book model
from .models import Book
# Import our BookSerializer
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    """
    API view that returns a list of all books in the database.
    
    Permission: IsAuthenticatedOrReadOnly
    - Anyone can view (GET) the list of books
    - Only authenticated users could modify (but this view doesn't allow modifications)
    
    URL: /api/books/
    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Override the default permission for this view
    # IsAuthenticatedOrReadOnly allows:
    # - Anyone (authenticated or not) to read (GET)
    # - Only authenticated users to write (POST, PUT, DELETE)
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing ALL CRUD operations on Book objects.
    
    Permission: IsAuthenticatedOrReadOnly
    - Anyone can LIST and RETRIEVE books (GET requests)
    - Only authenticated users can CREATE, UPDATE, or DELETE books
    
    This provides a good balance between open access and security:
    - Public users can browse books
    - Only registered users can modify the collection
    
    Endpoints:
    - GET    /api/books_all/        - List all books (public)
    - POST   /api/books_all/        - Create book (requires auth)
    - GET    /api/books_all/{id}/   - Get specific book (public)
    - PUT    /api/books_all/{id}/   - Update book (requires auth)
    - PATCH  /api/books_all/{id}/   - Partial update (requires auth)
    - DELETE /api/books_all/{id}/   - Delete book (requires auth)
    """
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Set permissions for this ViewSet
    # IsAuthenticatedOrReadOnly means:
    # - GET requests (list, retrieve) work for everyone
    # - POST, PUT, PATCH, DELETE require authentication
    permission_classes = [IsAuthenticatedOrReadOnly]
