# Creating Book Instances Using Django ORM

Below are examples of how to create new `Book` instances in the Django shell using the ORM.

```python
# Open the Django shell
python manage.py shell

# Import the Book model
from book_store.models import Book

# Create new book records
Book.objects.create(
    title="The Pragmatic Programmer",
    author="William A",
    publication_year=2000
)
# Expected output: <Book: The Pragmatic Programmer> successfully created

Book.objects.create(
    title="Clean Code",
    author="Robert C. Martin",
    publication_year=2008
)
# Expected output: <Book: Clean Code> successfully created