# Generated by Django 4.2.3 on 2023-08-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.FloatField(unique=True, verbose_name='версия карточки продукта')),
                ('version_name', models.CharField(max_length=50, verbose_name='название версии')),
                ('is_active', models.BooleanField(default=False, verbose_name='активная ли версия?')),
                ('product', models.ManyToManyField(to='catalog.product', verbose_name='продукты')),
            ],
            options={
                'verbose_name': 'версия товара',
                'verbose_name_plural': 'версии товаров',
            },
        ),
    ]