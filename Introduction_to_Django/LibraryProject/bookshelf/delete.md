# Deleting Book Instances Using Django ORM


```python
# Open the Django shell
python manage.py shell

# Import the Book model
from bookshelf.models import Book

# Retrieve the book you want to delete
# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by listing all books
books = Book.objects.all()
print(books)


# Expected Output: <QuerySet [<Book: Book object (2)>, <Book: Book object (3)>]>