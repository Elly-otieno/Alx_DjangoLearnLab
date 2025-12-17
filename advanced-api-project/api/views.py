from django.shortcuts import render
from .models import Book
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, permissions, filters
from .serializers import BookSerializer
# Create your views here.

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['id', 'title', 'publication_year', 'author']
    template_name = 'book_form.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    ordering = ['-publication_year']


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book-list')
    login_url = '/login/'

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'book_update.html'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.Is_Authenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]


class BookDeleteView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.Is_Authenticated]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

class BookUpdateView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.Is_Authenticated]