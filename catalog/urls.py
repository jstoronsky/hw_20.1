from django.urls import path
from catalog.views import show_contacts, ProductDetailView, HomepageListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, VersionCreateView
from catalog.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
               path('contacts/', show_contacts, name='contacts'),
               path('', HomepageListView.as_view(), name=''),
               path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
               path('create/', ProductCreateView.as_view(), name='create'),
               path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
               path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
               path('createversion/', VersionCreateView.as_view(), name='createversion'),
               ]
