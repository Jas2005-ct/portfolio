from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Creates a superuser if none exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # username = os.environ.get('DJANGO_SUPERUSER_USERNAME') # Not used for lookup if email is USERNAME_FIELD
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not User.objects.filter(email=email).exists():
            if email and password:
                # For custom user models, we might not need username, or it might be a separate field
                # If your create_superuser method requires username, pass it. 
                # Assuming standard custom user where email is key:
                try:
                    User.objects.create_superuser(email=email, password=password)
                    self.stdout.write(self.style.SUCCESS(f'Superuser "{email}" created successfully'))
                except TypeError:
                     # Fallback if the model still requires a username field
                    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
                    User.objects.create_superuser(username=username, email=email, password=password)
                    self.stdout.write(self.style.SUCCESS(f'Superuser "{email}" created successfully'))
            else:
                self.stdout.write(self.style.WARNING('Superuser details not found in environment variables'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superuser "{email}" already exists'))
