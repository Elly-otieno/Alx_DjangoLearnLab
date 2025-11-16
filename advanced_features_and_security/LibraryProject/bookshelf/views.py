from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .forms import BookForm 
from .models import Book
# from django.http import HttpResponseForbidden 


# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookshelf/view_book.html', {'book': book})


@permission_required('bookshelf.can_edit', raise_exception=True) 
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user.has_perm('bookshelf.can_edit'):
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
    if request.user.has_perm('bookshelf.can_delete'):
        book.delete()
        return redirect('books')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True) 
def create_book(request):
    if request.user.has_perm('bookshelf.can_create'):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})


'''
using has_perm

def view_book(request, book_id):
    if not request.user.has_perm('bookshelf.can_view'):
        return HttpResponseForbidden("You do not have permission to view this book.")

    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookshelf/view_book.html', {'book': book})


def edit_book(request, book_id):
    if not request.user.has_perm('bookshelf.can_edit'):
        return HttpResponseForbidden("You do not have permission to edit this book.")

    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)

    return render(request, 'bookshelf/edit_book.html', {'form': form})


def delete_book(request, book_id):
    if not request.user.has_perm('bookshelf.can_delete'):
        return HttpResponseForbidden("You do not have permission to delete this book.")

    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        book.delete()
        return redirect('books')

    return render(request, 'bookshelf/delete_book.html', {'book': book})


def create_book(request):
    if not request.user.has_perm('bookshelf.can_create'):
        return HttpResponseForbidden("You do not have permission to create a new book.")

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()

    return render(request, 'bookshelf/add_book.html', {'form': form})
'''