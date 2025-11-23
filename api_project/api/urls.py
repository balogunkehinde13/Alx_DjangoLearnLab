from django.urls import path, include
# Import the DefaultRouter for automatically generating URLs
from rest_framework.routers import DefaultRouter
# Import the built-in token authentication view
from rest_framework.authtoken.views import obtain_auth_token
# Import our views
from .views import BookList, BookViewSet

# Create a router instance
router = DefaultRouter()

# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns for the api app
urlpatterns = [
    # Route for the BookList view (ListAPIView - read-only, returns all books)
    path('books/', BookList.as_view(), name='book-list'),
    
    # Token authentication endpoint
    # Users POST their username and password here to get a token
    # Example: POST /api/token/ with {"username": "john", "password": "secret123"}
    # Response: {"token": "abc123xyz456..."}
    path('token/', obtain_auth_token, name='api-token-auth'),
    
    # Include ALL the router URLs for BookViewSet (full CRUD operations)
    path('', include(router.urls)),
]