from django.urls import path
from catalog.views import show_home_page, show_contacts

urlpatterns = [path('', show_contacts), path('', show_home_page)]

