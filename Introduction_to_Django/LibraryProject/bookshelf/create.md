# Creating Book Instances Using Django ORM

Below are examples of how to create new `Book` instances in the Django shell using the ORM.

```python
# Open the Django shell
python manage.py shell

# Import the Book model
from bookshelf.models import Book

# Create new book records
Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
# Expected output: <Book: Book object (4)>