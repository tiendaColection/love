from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='liset').exists():
            User.objects.create_superuser('admin', 'noequispeliset@gmail.com', '1981mayo23')
            print("Superusuario creado con éxito")
        else:
            print("El superusuario ya existe")