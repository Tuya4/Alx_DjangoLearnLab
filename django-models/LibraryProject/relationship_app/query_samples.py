from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

if __name__ == '__main__':
    get_books_by_author('George Orwell')
    get_books_in_library('Central Library')
    get_librarian_of_library('Central Library')

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