from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Figurine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='Imagen')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    id_art = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name