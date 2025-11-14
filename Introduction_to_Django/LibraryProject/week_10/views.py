from django.shortcuts import render
from django.http import HttpResponse
from week_10.models import Book
from django.urls import reverse_lazy


from django.views.generic import TemplateView, DetailView, UpdateView

# Create your views here.

# FUNCTION BASED VIEWS

def hello_view(request):
    '''A basic function view returning a greeting message.'''
    return HttpResponse('Hello, World!')

def book_list(request):
    '''Retrieves all books and renders a template displaying the list'''
    books = Book.objects.all() # fetch all book instances from db
    context = {'book_list': books} # create a context dictionary with a book list
    return render(request, 'book/book_list.html', context)


# CLASS BASED VIEWS 

class HelloView(TemplateView):
    '''A class based view rendering a template nammed 'hello.html'.'''
    template_name = 'hello.html'

class BookDetailView(DetailView):
    '''A class-based view for displaying details of a specific book.'''
    model = Book
    template_name = 'books/book_detail.html'

    def get_context_data(self, **kwargs):
        '''Injects additional context data specific to the book'''
        context = super().get_context_data(**kwargs) # Get default context data
        book = self.get_object() # Retrieve the currebt book instance
        context['average_rating'] = book.get_average_rating()     # assuming the method 'get_average_rating' exists on book instance


class BookUpdateView(UpdateView):
    '''A class based view for updating details of a specific book '''
    model = Book
    fields = ['title', 'author', 'description'] # specify fields to be editable
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('book_list') # URL to redirect after succesful update
    
    def form_valid(self, form):
        '''Executes custom logic after form validation'''
        response = super().form_valid(form)  # Call default form validatiom
        # Perform additional actions after successful update e.g send notifications
        return response