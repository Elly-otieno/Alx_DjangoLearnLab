from django.shortcuts import render, redirect
from .serializers import PostSerializer
# from rest_framework import generics
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostForm

# Create your views here.

class PostDisplayView(ListView):
    model = Post
    template_name = ''
    context_object_name = ''

class PostDetailView(DetailView):
    model = Post
    template_name = ''
    context_object_name = ''

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'content', 'author', 'published_date'] 
    template_name = 'add_post.html'
    login_url = '/login/'
    success_url = reverse_lazy('posts')

    # def form_valid(self, form):
    #     form.instance.author = self.request.save()
    #     return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user # pass logged-in user to form
        return kwargs
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = ''
    # fields = ['title', 'content', 'author', 'published_date']
    login_url = '/login/'
    success_url = reverse_lazy('posts')

    # def form_valid(self, form):
    #     form.instance.author = self.request.save()
    #     return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = ''
    login_url = ''
    success_url = reverse_lazy('post-list')