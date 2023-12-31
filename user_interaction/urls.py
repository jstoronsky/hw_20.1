from django.contrib.auth.views import LogoutView
from django.urls import path
from user_interaction.apps import UserInteractionConfig
from user_interaction.views import RegisterView, ChangeView, UserLogin, \
    activate_email, reset_password

app_name = UserInteractionConfig.name

urlpatterns = [path('register/', RegisterView.as_view(), name='register'),
               path('login/', UserLogin.as_view(), name='login'),
               path('logout/', LogoutView.as_view(), name='logout'),
               path('profile/', ChangeView.as_view(), name='profile'),
               path('activate/', activate_email, name='activate'),
               path('reset/', reset_password, name='reset'),
               path('success_reset/', reset_password, name='successful_reset'),
               path('error_reset/', reset_password, name='error_reset')
               ]
