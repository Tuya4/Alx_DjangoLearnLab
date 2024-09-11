from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializes Book objects
class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author_name']

    def validate_publication_year(self, value): # Validation to ensure the publication year is not from the future
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

# Serializes Author objects along with their related books
# Uses nested serialization to include related Book objects
class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    
    def to_representation(self, instance): 
        representation =  super().to_representation(instance)  
        representation['books'] = BookSerializer(instance.books.all(), many=True).data
        return representation          