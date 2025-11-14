from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name

author1 = Author.objects.create(name="Elly Okoth")
author2 = Author.objects.create(name="Elly Senior")
book1 = Book.objects.create(name='Django for Beginners', author=author1)
book2 = Book.objects.create(name='Django Advanced', author=author2)
# library1=Library.objects.create(name='Computing', books=[book1, book2])
# library2= Library.objects.create(name='Technology', books=[book2])

library1 = Library.objects.create(name='Computing')
library1.books.set([book1, book2])
# library1.books.add(book1, book2)

library2 = Library.objects.create(name='Technology')
library2.books.set([book2])

librarian1 = Librarian.objects.create(name='Tech guy', library=library2)
librarian2 = Librarian.objects.create(name='Tech Senior', library=library1)
