from django.shortcuts import render
from catalog.models import Product, Contacts
from django.http import HttpResponseRedirect


# Create your views here.


def show_admin(request):
    return HttpResponseRedirect('http://127.0.0.1:8000/admin/')


def show_home_page(request):
    products = Product.objects.all()[:5]
    to_html_dict = {}
    for index in range(len(products)):
        to_html_dict[f'product{index + 1}'] = products[index]
        to_html_dict[f'price{index + 1}'] = products[index].price
        to_html_dict[f'desc{index + 1}'] = products[index].description
    print(products)
    return render(request, 'main/home_page.html', to_html_dict)


def show_contacts(request):
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_email = request.POST.get('email')
        get_message = request.POST.get('message')
        print(f'Имя: {get_name}, email: {get_email}\n Сообщение: {get_message}')
    company = Contacts.objects.all()
    to_html_dict = {}
    for information in company:
        to_html_dict['company_name'] = information
        to_html_dict['address'] = information.address
        to_html_dict['email'] = information.email
        to_html_dict['number'] = information.number
        to_html_dict['desc'] = information.description
    return render(request, 'main/contacts.html', to_html_dict)
