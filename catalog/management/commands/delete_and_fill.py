from django.core.management import BaseCommand
from catalog.models import Product, Category
import json


class Command(BaseCommand):
    def handle(self, file='./catalog.json', *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open(file) as jsn_file:
            python_type = json.load(jsn_file)
        categories = [item['fields'] for item in python_type if 'product_name' not in item['fields'].keys()]
        categories_to_fill = []
        for number, category in enumerate(categories):
            categories_to_fill.append(Category(pk=number + 1, **category))
        Category.objects.bulk_create(categories_to_fill)

        products = [item['fields'] for item in python_type if 'category_name' not in item['fields'].keys()]
        for pro in products:
            pro['category'] = Category.objects.get(pk=pro['category'])
        products_to_fill = []
        for number_, product in enumerate(products):
            products_to_fill.append(Product(pk=number_ + 1, **product))
        Product.objects.bulk_create(products_to_fill)
