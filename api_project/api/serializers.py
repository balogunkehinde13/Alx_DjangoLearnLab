from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Converts Book model instances to JSON format (serialization)
    and JSON data to Book model instances (deserialization).
    """
    
    class Meta:
        # Specify which model this serializer is for
        model = Book
        
        # Include all fields from the Book model
        # This will automatically include: id, title, author, publication_year
        fields = '__all__'