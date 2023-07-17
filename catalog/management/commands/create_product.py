from django.core.management import BaseCommand
from catalog.models import Product, Category
from datetime import date


class Command(BaseCommand):
    def handle(self, *args, **options):
        products_len = len(Product.objects.all())
        Product.objects.create(pk=products_len + 1, product_name=input('Введите наименование продукта: '),
                               description=input('Описание: '),
                               category=Category.objects.get(pk=int(input('Введите номер категории(1-Напитки, 2-Фрукты и овощи 3-Орехи и сухофрукты): '))),
                               price=int(input('Введите цену: ')), date_when_added=date.today(),
                               date_when_changed=date.today())
