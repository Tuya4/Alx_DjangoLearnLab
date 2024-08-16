import django
from django.conf import settings
from django.core.management import execute_from_command_line
from relationship_app.models import Author, Book, Library, Librarian

settings.configure(
    DEBUG=True,
    INSTALLED_APPS=[
        'relationship_app',
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bookshelf',
            'USER': 'root',
            'PASSWORD': 'Bazenga@3314',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    },
)
django.setup()

def query_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    for book in books:
        print(f'Book Title: {book.title}')

def list_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f'Book Title: {book.title}')

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f'Librarian Name: {librarian.name}')

if __name__ == '__main__':
    query_all_books_by_author('George Orwell')
    list_all_books_in_library('Central Library')
    retrieve_librarian_for_library('Central Library')

# def query_books_by_author(author_name):
#     books = Book.objects.filter(author_name=author_name)
#     return books

# def  list_books_in_library(library_name):
#     library = Library.objects.get(name=library_name)
#     books = library.books.all()
#     return books

# def retrieve_librarian_for_library(library_name):
#     try:
#         library = Library.objects.get(name=library_name)
#         librarian = Librarian.objects.get(library=library)
#         return librarian
#     except Librarian.DoesNotExist:
#         return None
    
#     # if __name__ == "__main__":
#     #     author_books = query_books_by_author("George Orwell")
#     #     print(f"Books by John Doe: {[book.title for book in author_books]}")

#     #     library_books = list_books_in_library("Central Library")
#     #     print(f"Books in Central Library: {[book.title for book in library_books]}")

#     #     librarian = retrieve_librarian_for_library("Central Library")
#     #     if librarian:
#     #         print(f"Librarian of Central Library: {librarian.name}")
#     #     else:
#     #         print("No librarian found for Central Library")