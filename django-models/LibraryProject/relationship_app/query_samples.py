from models import Author, Book, Library, Librarian

'''
Query all books by a specific author.
List all books in a library.
Retrieve the librarian for a library.
'''

# book_in_library1 = library1.books.all()


# Query all books by a specific author.
def get_book_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library.
def list_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    return books_in_library


# Retrieve the librarian for a library.
def get_librarian(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian.name
    return librarian

