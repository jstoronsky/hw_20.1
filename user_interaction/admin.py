from django.contrib import admin
from user_interaction.models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'number', 'avatar', 'number', 'country')
