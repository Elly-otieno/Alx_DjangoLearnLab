
# Django Permissions

Using **Django’s built-in permissions** with function-based views using the `@permission_required` decorator.

## Features
- Custom permissions added through the `Book` model (`view_book`, `add_book`, `change_book`, `delete_book`)
- Permission checks in views using:

  ```python
  @permission_required("bookshelf.view_book", raise_exception=True)
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
```


# Security Review 

## Changes implemented
- DEBUG disabled for production (DEBUG=False)
- SECRET_KEY moved to environment variables
- HTTPS enforced via SECURE_SSL_REDIRECT + Nginx redirect
- HSTS enabled (SECURE_HSTS_SECONDS)
- Cookies secured: SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE, SESSION_COOKIE_HTTPONLY
- Browser protections: SECURE_CONTENT_TYPE_NOSNIFF, SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS=DENY
- CSP header implemented (django-csp recommended)
- All forms include {% csrf_token %} and use Django Forms for validation
- ORM used for queries; no raw SQL used without parameterization


