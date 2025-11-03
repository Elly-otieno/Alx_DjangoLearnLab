# Updating Book Instances Using Django ORM

Below is an example of how to update an existing book record in the Django shell.

```python
# Open the Django shell
python manage.py shell

# Import the Book model
from book_store.models import Book

# Retrieve the book you want to update
book = Book.objects.get(title="The Pragmatic Programmer")

# Update the title of the book
book.title = "The Pragmatic Programmer (Revised Edition)"
book.save()

# Verify the change
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)
# Expected output: The Pragmatic Programmer (Revised Edition)
