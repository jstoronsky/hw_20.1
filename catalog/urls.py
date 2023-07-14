from django.urls import path
from catalog.views import show_home_page, show_contacts, show_admin

urlpatterns = [path('', show_admin)]  # отображение админки
# urlpatterns = [path('', show_contacts)]  # отображение страницы с контактными данными
# urlpatterns = [path('', show_home_page)]  # главная страница
