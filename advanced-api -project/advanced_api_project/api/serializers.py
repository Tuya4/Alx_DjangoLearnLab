from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer): 

    books = BookSerializer(many=True, read_only=True) 
  # Nested serializer for books

    class Meta:
        model = Author
        fields = ['name', 'books']    