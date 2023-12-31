from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductAddForm, ProductEditForm, VersionCreateForm
from catalog.models import Product, Contacts, Category, Version
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from catalog.service import cached_categories


# Create your views here.
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductAddForm
    # fields = ('product_name', 'description', 'category', 'price', 'date_when_added', 'date_when_changed')
    success_url = reverse_lazy('catalog:')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductEditForm
    # fields = ('product_name', 'description', 'price', 'date_when_changed')
    success_url = reverse_lazy('catalog:')
    permission_required = ('catalog.set_is_active', 'catalog.change_product_description',
                           'catalog.change_product_category')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_form_set = inlineformset_factory(Product, Version, form=VersionCreateForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = version_form_set(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = version_form_set(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        object_ = form.save()
        if formset.is_valid():
            formset.instance = object_
            formset.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        object_ = super().get_object(queryset)
        if object_.user != self.request.user and not self.request.user.is_superuser:
            raise Http404('Вы не можете редактировать данный товар')
        return object_


class HomepageListView(ListView):
    model = Product
    template_name = 'catalog/home_page.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        all_products = Product.objects.all()
        products = [product.id for product in all_products]
        for product in products:
            for version in Version.objects.filter(product=product):
                max_version = max([vers.version_number for vers in Version.objects.filter(product=product)])
                if version.version_number == max_version:
                    version.is_active = True
                else:
                    version.is_active = False
                version.save(update_fields=['is_active'])
        context_data['versions'] = Version.objects.filter(is_active=True)
        context_data['categories'] = cached_categories
        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)


def show_contacts(request):
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_email = request.POST.get('email')
        get_message = request.POST.get('message')
        print(f'Имя: {get_name}, email: {get_email}\n Сообщение: {get_message}')
    company = Contacts.objects.all()

    products = Product.objects.all()
    to_html_dict = {'categories': cached_categories(), 'object_list': products}
    for information in company:
        to_html_dict['company_name'] = information
        to_html_dict['address'] = information.address
        to_html_dict['email'] = information.email
        to_html_dict['number'] = information.number
        to_html_dict['desc'] = information.description
    return render(request, 'catalog/contacts.html', to_html_dict)


# def edit_base_template(request):
#     categories = Category.objects.all()
#     products = Product.objects.all()
#     to_html_dict = {'categories': categories, 'products': products}
#     return render(request, 'catalog/base_sidebar', to_html_dict)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        products = Product.objects.all()
        context_data['object_list'] = products
        context_data['categories'] = cached_categories()
        return context_data


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionCreateForm
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
