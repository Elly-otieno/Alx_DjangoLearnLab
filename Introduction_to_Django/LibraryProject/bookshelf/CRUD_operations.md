# Django ORM CRUD Operations

## Create Operation

```python

In [3]: from bookshelf.models import Book
   ...:
   ...: # Create new book records
   ...: Book.objects.create(
   ...:     title="1984",
   ...:     author="George Orwell",
   ...:     publication_year=1949
   ...: )
Out[3]: <Book: Book object (4)>
```

## Retrieve Operation

```python

In [4]: # Retrieve and display all attributes of the created book
   ...: book = Book.objects.get(title="1984")
   ...: print(book.title, book.author, book.publication_year)
1984 George Orwell 1949
```

## Update Operation

```python

In [5]: # Update the book title
   ...: book = Book.objects.get(title="1984")
   ...: book.title = "Nineteen Eighty-Four"
   ...: book.save()
   ...:
   ...: # Confirm update
   ...: updated_book = Book.objects.get(id=book.id)
   ...: print(updated_book.title)
Nineteen Eighty-Four
```

## Delete Operation

```python

In [6]: # Delete the book
   ...: book = Book.objects.get(title="Nineteen Eighty-Four")
   ...: book.delete()
   ...:
   ...: # Confirm deletion by listing all books
   ...: books = Book.objects.all()
   ...: print(books)
<QuerySet [<Book: Book object (2)>, <Book: Book object (3)>]>
```