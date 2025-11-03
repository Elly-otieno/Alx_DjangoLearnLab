# Django ORM CRUD Operations

This document shows how to perform **Create**, **Retrieve**, **Update**, and **Delete** operations on the `Book` model using the Django shell.

---

## Create Operation

```python

In [9]: Book.objects.create(
   ...: title="The Pragmatic Programmer",
   ...: author="William A",
   ...: publication_year= 2000
   ...: )
Out[9]: <Book: Book object (1)>

In [10]: Book.objects.create(
    ...:     title="Clean Code",
    ...:     author="Robert C. Martin",
    ...:     publication_year=2008
    ...: )
Out[10]: <Book: Book object (2)>

In [11]: Book.objects.create(
    ...:     title="Design Patterns: Elements of Reusable Object-Oriented Software",
    ...:     author="Erich Gamma",
    ...:     publication_year=1994
    ...: )
Out[11]: <Book: Book object (3)>
```

## Retrieve Operation

```python

# Retrieve all books
In [12]: Book.objects.all()
    ...:
Out[12]: <QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>]>

In [13]: books = Book.objects.all()
    ...: print(books)
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>]>


# Retrieve a single book by title

In [14]: book = Book.objects.get(title="Clean Code")
    ...: print(book.title, book.author, book.publication_year)
Clean Code Robert C. Martin 2008

# Filter books published after the year 2000

In [15]: recent_books = Book.objects.filter(publication_year__gt=2000)
    ...: for b in recent_books:
    ...:     print(b.title, b.publication_year)
    ...:
Clean Code 2008

# Filter books by id
In [16]: book = Book.objects.get(id=1)
    ...: print(book.title, book.author)
The Pragmatic Programmer William A
```

## Update Operation

```python

# Update the title of an existing book

In [17]: book = Book.objects.get(title="The Pragmatic Programmer")
    ...:
    ...: # Update the title of the book
    ...: book.title = "The Pragmatic Programmer (Revised Edition)"
    ...: book.save()

# Confirm the update
In [18]: updated_book = Book.objects.get(id=book.id)
    ...: print(updated_book.title)
The Pragmatic Programmer (Revised Edition)
```

## Delete Operation

```python

# Delete a book
In [19]: book = Book.objects.get(title="The Pragmatic Programmer (Revised Edition)")
    ...:
    ...: # Delete the book
    ...: book.delete()
Out[19]: (1, {'bookshelf.Book': 1})

# Confirm deletion
In [20]: Book.objects.filter(title="The Pragmatic Programmer (Revised Edition)").exists()
Out[20]: False
```