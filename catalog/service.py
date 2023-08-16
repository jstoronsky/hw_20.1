from django.core.cache import cache

from catalog.models import Product
from config import settings


def cached_categories():
    """
    функция для кэширования списка категорий
    """
    products = Product.objects.all()
    actual_categories = list(set([product.category for product in products]))

    if settings.CACHE_ENABLED:
        key = 'categories_list'
        categories = cache.get(key)
        if categories is None:
            categories = actual_categories
            cache.set(key, categories)
    else:
        categories = actual_categories
    return categories
