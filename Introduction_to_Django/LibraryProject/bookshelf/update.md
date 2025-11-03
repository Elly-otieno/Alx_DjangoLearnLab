# Updating Book Instances Using Django ORM

Below is an example of how to update an existing book record in the Django shell.

```python
# Open the Django shell
python manage.py shell

# Import the Book model
from bookshelf.models import Book

# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title)

# Expected Output: Nineteen Eighty-Four
