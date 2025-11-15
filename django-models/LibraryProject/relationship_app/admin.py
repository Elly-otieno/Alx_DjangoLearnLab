from django.contrib import admin
from .models import Book, Author, Library, Librarian

# Register models here

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    # list_filter = ('author')  

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)