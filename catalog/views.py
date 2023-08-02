from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductAddForm, ProductEditForm
from catalog.models import Product, Contacts, Category
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


# Create your views here.
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductAddForm
    # fields = ('product_name', 'description', 'category', 'price', 'date_when_added', 'date_when_changed')
    success_url = reverse_lazy('catalog:')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductEditForm
    # fields = ('product_name', 'description', 'price', 'date_when_changed')
    success_url = reverse_lazy('catalog:')


class HomepageListView(ListView):
    model = Product
    template_name = 'catalog/home_page.html'


def show_contacts(request):
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_email = request.POST.get('email')
        get_message = request.POST.get('message')
        print(f'Имя: {get_name}, email: {get_email}\n Сообщение: {get_message}')
    company = Contacts.objects.all()
    categories = Category.objects.all()
    to_html_dict = {'categories': categories}
    for information in company:
        to_html_dict['company_name'] = information
        to_html_dict['address'] = information.address
        to_html_dict['email'] = information.email
        to_html_dict['number'] = information.number
        to_html_dict['desc'] = information.description
    return render(request, 'catalog/contacts.html', to_html_dict)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:')


# def show_home_page(request):
#     products = Product.objects.all()
#     categories = Category.objects.all()
#     to_html_dict = {'object_list': products,
#                     'categories': categories}
#     # for index in range(len(products)):
#     #     to_html_dict[f'product{index + 1}'] = products[index]
#     #     to_html_dict[f'price{index + 1}'] = products[index].price
#     #     to_html_dict[f'desc{index + 1}'] = products[index].description
#     print(products)
#     return render(request, 'catalog/home_page.html', to_html_dict)

# def show_product(request):
#     products = Product.objects.all()
#     categories = Category.objects.all()
#     to_html_dict = {'object_list': products,
#                     'categories': categories}
#     return render(request, 'catalog/product_detail.html', to_html_dict)
