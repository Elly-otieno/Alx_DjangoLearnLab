# Retrieving Book Instances Using Django ORM

Below are examples of how to retrieve and display book details in the Django shell.

```python
# Open the Django shell
python manage.py shell

# Import the Book model
from book_store.models import Book

# Retrieve all books
books = Book.objects.all()
print(books)
# Expected output: <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>]>

# Retrieve a single book by title
book = Book.objects.get(title="Clean Code")
print(book.title, book.author, book.publication_year)
# Expected output: Clean Code Robert C. Martin 2008

# Retrieve books published after the year 2000
recent_books = Book.objects.filter(publication_year__gt=2000)
for b in recent_books:
    print(b.title, b.publication_year)
# Expected output: Clean Code 2008

# Retrieve a specific book by ID
book = Book.objects.get(id=1)
print(book.title, book.author)
# Expected output: The Pragmatic Programmer William A
