from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование товара')
    description = models.TextField(verbose_name='описание товара')
    product_image = models.ImageField(upload_to='products/', verbose_name='изображение продукта', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='цена товара')
    date_when_added = models.DateField(auto_now=False, auto_now_add=False,
                                       verbose_name='дата добавления товара на сайт')
    date_when_changed = models.DateField(auto_now=False, auto_now_add=False,
                                         verbose_name='дата изменения информации по товару')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('id', )


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование категории')
    description = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('id', )
