from django.shortcuts import render
from models import Book
from .models import Library

# from django.views.generic import DetailView
from django.views.generic.detail import DetailView

# Create your views here.

def list_all_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class display_library_details(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
