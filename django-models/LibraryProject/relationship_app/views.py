from django.shortcuts import render
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login


# from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import redirect


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

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log in the newly registered user
        messages.success(self.request, "Registration successful. You're now logged in.")
        return redirect('books')  # Or wherever you want to redirect


class CustomLoginView(LoginView):
    template_name= 'relationship_app/login.html'
    success_url = reverse_lazy('books')

    def get_success_url(self):
        return reverse_lazy('books')  # overrides any ?next= parameter



class CustomLogoutView(LogoutView):
    template_name= 'relationship_app/logout.html'
    success_url = reverse_lazy('login')