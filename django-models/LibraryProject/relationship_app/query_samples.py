from models import Author, Book, Library, Librarian

'''
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.
'''

# book_in_library1 = library1.books.all()


# Query all books by a specific author.


author = Author.objects.get(name='Elly Okoth')
books = author.books.all()

# List all books in a library.
library_name = 'Technology'
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# Retrieve the librarian for a library.
library = Library.objects.get(name='Computing')
librarian = library.librarian.name