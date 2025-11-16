from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ExampleForm, BookForm
from .models import Book


# Create your views here.

# @permission_required('bookshelf.can_view', raise_exception=True)
# def view_book(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     return render(request, 'bookshelf/view_book.html', {'book': book})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_edit', raise_exception=True) 
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})


@permission_required('bookshelf.can_delete', raise_exception=True) 
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True) 
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})


# Safe search view using Django Form validation and ORM
@permission_required('bookshelf.can_view', raise_exception=True)
def book_search(request):
    form = ExampleForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        q = form.cleaned_data.get('q', '').strip()
        if q:
            # Using ORM parameterization to avoid SQL injection
            books = Book.objects.filter(title__icontains=q).order_by('publication_year')
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})