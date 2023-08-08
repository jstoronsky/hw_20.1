from django.core.management import BaseCommand

from user_interaction.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        superuser = CustomUser.objects.create(
            email='jstoronsky@gmail.com',
            first_name='Admin',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        superuser.set_password('Demon6600')
        superuser.save()
