from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView , CreateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
class PostDetailView(DetailView):
    model = Post
    template_name = 'detail_view.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'Post_new.html'
    fields = ['title', 'author', 'body']
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name= "post_delete.html"
    success_url= reverse_lazy('home')
