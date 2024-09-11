from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author_name']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['books'] = BookSerializer(instance.books.all(), many=True).data
        return representation