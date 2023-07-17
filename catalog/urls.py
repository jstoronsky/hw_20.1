from django.urls import path
from catalog.views import show_home_page, show_contacts, show_product
from catalog.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
               path('contacts', show_contacts, name='contacts'),
               path('', show_home_page, name=''),
               path('product', show_product, name='product'),
               ]
