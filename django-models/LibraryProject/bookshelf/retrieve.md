# Retrieving Book Instances Using Django ORM


```python
# Open the Django shell
python manage.py shell

# Import the Book model
from bookshelf.models import Book

# Retrieve and display all attributes of the created book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# Expected Output: 1984 George Orwell 1949