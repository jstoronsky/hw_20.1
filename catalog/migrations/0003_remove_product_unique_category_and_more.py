# Generated by Django 4.2.3 on 2023-07-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='product',
            name='unique category',
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('id',), name='unique category'),
        ),
    ]
