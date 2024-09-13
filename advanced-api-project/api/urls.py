from django.urls import path
from .views import BookListView, BookDetailView
from . import views

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),  # Create new book
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),  # Update book
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # Delete book
]