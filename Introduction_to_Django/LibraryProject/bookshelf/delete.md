# Deleting Book Instances Using Django ORM

Below is an example of how to delete a book record from the database using the Django shell.

```python
# Open the Django shell
python manage.py shell

# Import the Book model
from book_store.models import Book

# Retrieve the book you want to delete
book = Book.objects.get(title="The Pragmatic Programmer (Revised Edition)")

# Delete the book
book.delete()

# Expected output: (1, {'book_store.Book': 1})
# This confirms that one Book instance was deleted from the database.

# Verify deletion
`Book.objects.filter(title="The Pragmatic Programmer (Revised Edition)").exists()`
# Expected output: False  → confirms the book has been successfully deleted.
