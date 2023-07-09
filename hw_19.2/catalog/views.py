from django.shortcuts import render
# Create your views here.


def show_home_page(request):
    return render(request, 'main/home_page.html')


def show_contacts(request):
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_email = request.POST.get('email')
        get_message = request.POST.get('message')
        print(f'Имя: {get_name}, email: {get_email}\n Сообщение: {get_message}')
    return render(request, 'main/contacts.html')
