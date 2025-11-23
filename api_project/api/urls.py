from django.urls import path
from .views import BookList

# Define URL patterns for the api app
urlpatterns = [
    # When someone visits /books/, call the BookList view
    # .as_view() converts the class-based view into a callable view function
    # name='book-list' allows us to reference this URL by name elsewhere
    path('books/', BookList.as_view(), name='book-list'),
]
