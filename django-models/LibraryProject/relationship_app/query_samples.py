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
    librarian = Librarian.objects.get(library=library_name)
    return librarian

'''
from relationship_app.models import Author, Book, Library, Librarian
author1 = Author.objects.create(name="Elly Okoth")
author2 = Author.objects.create(name="Elly Senior")
book1 = Book.objects.create(title='Django for Beginners', author=author1)
book2 = Book.objects.create(title='Django Advanced', author=author2)
# library1=Library.objects.create(name='Computing', books=[book1, book2])
# library2= Library.objects.create(name='Technology', books=[book2])

library1 = Library.objects.create(name='Computing')
library1.books.set([book1, book2])
# library1.books.add(book1, book2)

library2 = Library.objects.create(name='Technology')
library2.books.set([book2])

librarian1 = Librarian.objects.create(name='Tech guy', library=library2)
librarian2 = Librarian.objects.create(name='Tech Senior', library=library1)

'''