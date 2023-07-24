from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from pytils.translit import slugify

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('header', 'content', 'preview', 'date_when_created', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid:
            slug = form.save()
            slug.link = slugify(slug.header)
            slug.save()
            return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('header', 'content', 'preview', 'is_published')
    # success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid:
            slug = form.save()
            slug.link = slugify(slug.header)
            slug.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:article', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
