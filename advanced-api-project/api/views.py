from django.shortcuts import render
from rest_framework import generics, status
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

class BookListView(generics.ListCreateAPIView):
    
    # Retrieve a list of all books or create a new book.
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny] # Public access to list and create books

    def post(self, request, *args, **kwargs):
         
        # Handle the creation of a new book with custom validation.
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    # Retrieve, update, or delete a book by its ID.
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update or delete

    def put(self, request, *args, **kwargs):
        
        # Handle the update of an existing book with custom logic.
        
        return super().put(request, *args, **kwargs)
