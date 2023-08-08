from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    is_active = models.BooleanField(default=False)
    date_joined = None
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар пользователя', **NULLABLE)
    number = models.CharField(max_length=25, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='страна', **NULLABLE)
    verification_key = models.CharField(max_length=4, verbose_name='ключ для верификации', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
