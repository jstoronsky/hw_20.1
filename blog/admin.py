from django.contrib import admin
from blog.models import Blog

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'link', 'content', 'preview', 'date_when_created', 'is_published', 'views_count')
