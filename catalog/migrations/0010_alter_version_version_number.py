# Generated by Django 4.2.3 on 2023-08-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_rename_product_version_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.FloatField(unique=True, verbose_name='версия карточки продукта'),
        ),
    ]
