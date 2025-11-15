from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import BookForm 


# from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
# from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
# from django.http import HttpResponseForbidden 


# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

# class based sign up
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log in the newly registered user
        messages.success(self.request, "Registration successful. You're now logged in.")
        return redirect('books')  # Or wherever you want to redirect

# function based sign up
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# class CustomLoginView(LoginView):
#     template_name= 'relationship_app/login.html'
#     success_url = reverse_lazy('books')

#     def get_success_url(self):
#         return reverse_lazy('books')  # overrides any ?next= parameter



# class CustomLogoutView(LogoutView):
#     template_name= 'relationship_app/logout.html'
#     success_url = reverse_lazy('login')


# @login_required
# def dashboard(request):
#     if request.user.profile.role == 'Librarian':
#         return render(request, 'relationship_app/librarian_view.html')
#     elif request.user.profile.role == 'Member':
#         return render(request, 'relationship_app/member_view.html')
#     elif request.user.profile.role == 'Admin':
#         return render(request, 'relationship_app/admin_view.html')
#     else: 
#         return HttpResponseForbidden("You don't have permission to access this page")


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'profile') and  user.profile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Member'
    
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
