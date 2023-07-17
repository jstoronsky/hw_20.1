from django.shortcuts import render
from catalog.models import Product, Contacts, Category


# Create your views here.
def show_home_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    to_html_dict = {'object_list': products,
                    'categories': categories}
    # for index in range(len(products)):
    #     to_html_dict[f'product{index + 1}'] = products[index]
    #     to_html_dict[f'price{index + 1}'] = products[index].price
    #     to_html_dict[f'desc{index + 1}'] = products[index].description
    print(products)
    return render(request, 'main/home_page.html', to_html_dict)


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
    return render(request, 'main/contacts.html', to_html_dict)


def show_product(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    to_html_dict = {'object_list': products,
                    'categories': categories}
    return render(request, 'main/product_card.html', to_html_dict)
