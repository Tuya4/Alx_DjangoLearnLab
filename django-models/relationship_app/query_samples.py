from relationship_app.models import Author, Book, Library, Librarian

# Create an Author object
author = Author(name='J.K. Rowling')
author.save()

# Create a Book object
book = Book(title='Harry Potter', author=author)
book.save()

# Create a Library object
library = Library(name='Main')
library.save()

# Add the book to the library
library.books.add(book)

# Create a Librarian object
librarian = Librarian(name='Madam Pince', library=library)
librarian.save()

# Query all books in the library
books = library.books.all()
print('Books in the library:')
for book in books:
    print(book.title)

# Query the librarian of the library
librarian = library.librarian
print(f'Librarian of the library: {librarian.name}')

# Query the author of the book
author = book.author

print(f'Author of the book: {author.name}')
# Output:
# Books in the library:
# Harry Potter
# Librarian of the library: Madam Pince
# Author of the book: J.K. Rowling

