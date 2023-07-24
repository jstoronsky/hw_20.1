from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'link', 'content', 'preview', 'date_when_created')
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'link', 'content', 'preview', 'is_published')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
