from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm demonstrates secure form handling.
    It uses Django’s built-in validation and prevents
    unsafe or malformed data from being saved to the database.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
