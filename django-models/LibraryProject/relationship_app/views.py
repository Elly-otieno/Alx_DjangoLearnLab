from django.shortcuts import render
from models import Book, Library
from django.views.generic import DetailView

# Create your views here.

def list_all_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'list_books.html', context)

class display_library_details(DetailView):
    model = Library
    template_name = 'library_detail.html'
