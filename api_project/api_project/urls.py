from django.contrib import admin
from django.urls import path, include

# Main URL configuration for the entire project
urlpatterns = [
    # Admin panel route
    path('admin/', admin.site.urls),
    
    # Include all URLs from the api app
    # Any URL starting with 'api/' will be handled by api/urls.py
    # Examples:
    #   - 'api/books/' -> BookList view (read-only)
    #   - 'api/books_all/' -> BookViewSet (full CRUD)
    #   - 'api/books_all/1/' -> BookViewSet detail operations
    path('api/', include('api.urls')),
]