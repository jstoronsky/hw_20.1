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
    user = models.ForeignKey('user_interaction.CustomUser', on_delete=models.CASCADE, verbose_name='Пользователь')

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
        constraints = [
            models.UniqueConstraint(fields=['id'], name='unique category')
        ]


class Contacts(models.Model):
    company_name = models.CharField(max_length=50, verbose_name='название компании')
    description = models.TextField(verbose_name='описание')
    address = models.CharField(max_length=150, verbose_name='адрес')
    email = models.EmailField(max_length=100, verbose_name='e-mail')
    number = models.CharField(max_length=50, verbose_name='контактный номер')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.FloatField(verbose_name='версия карточки продукта')
    version_name = models.CharField(max_length=50, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='активная ли версия?')

    # def show_products(self):
    #     return ", ".join([p.product_name for p in self.products.all()])

    def __str__(self):
        return f'Версия {self.version_number} ({self.version_name})'

    class Meta:
        verbose_name = 'версия товара'
        verbose_name_plural = 'версии товаров'
