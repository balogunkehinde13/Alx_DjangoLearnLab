from django.urls import path, include
# Import the DefaultRouter for automatically generating URLs
from rest_framework.routers import DefaultRouter
# Import our views
from .views import BookList, BookViewSet

# Create a router instance
# The router will automatically generate URL patterns for our ViewSet
router = DefaultRouter()

# Register the BookViewSet with the router
# Arguments:
#   r'books_all' - The URL prefix for this ViewSet
#   BookViewSet - The ViewSet class to register
#   basename='book_all' - Base name for the URL patterns (used for reverse lookups)
# 
# This single registration creates these URLs automatically:
#   - GET    /books_all/          -> list all books
#   - POST   /books_all/          -> create a new book
#   - GET    /books_all/{id}/     -> retrieve a specific book
#   - PUT    /books_all/{id}/     -> update a specific book (all fields)
#   - PATCH  /books_all/{id}/     -> partial update (some fields)
#   - DELETE /books_all/{id}/     -> delete a specific book
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns for the api app
urlpatterns = [
    # Route for the BookList view (ListAPIView - read-only, returns all books)
    # This is our original simple view that only does GET requests
    path('books/', BookList.as_view(), name='book-list'),
    
    # Include ALL the router URLs for BookViewSet (full CRUD operations)
    # The empty string '' means these URLs start from the current path
    # Since we're in the 'api/' namespace, router URLs will be like:
    #   - /api/books_all/
    #   - /api/books_all/1/
    path('', include(router.urls)),
]
