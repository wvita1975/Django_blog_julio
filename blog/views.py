from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
class PostDetailView(DetailView):
    model = Post
    template_name = 'detail_view.html'
    