from django.shortcuts import render
from models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# from django.views.generic import DetailView
from django.views.generic.detail import DetailView, CreateView

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'