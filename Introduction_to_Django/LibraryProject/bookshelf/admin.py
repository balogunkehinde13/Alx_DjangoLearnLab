from django.contrib import admin
from .models import Book

# 1. Define the custom Admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    # Customize the columns displayed on the changelist page (list view)
    list_display = ('title', 'author', 'publication_year')

    # Add filters to the sidebar for easy filtering of data
    list_filter = ('author', 'publication_year')

    # Enable a search bar that searches across specified fields
    search_fields = ('title', 'author')

    # Make publication_year a link to the detail page (optional but useful)
    list_display_links = ('title', 'publication_year')
    
# 2. Register the model with the customized admin class
admin.site.register(Book, BookAdmin)