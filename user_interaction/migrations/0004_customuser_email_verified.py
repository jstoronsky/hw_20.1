# Generated by Django 4.2.3 on 2023-08-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_interaction', '0003_customuser_verification_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Account_vefield?'),
        ),
    ]