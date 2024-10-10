from django import forms
from .models import Figurine, Genre, Category

class FigurineForm(forms.ModelForm):
    class Meta:
        model = Figurine
        fields = ['name', 'description', 'category', 'genre', 'imagen', 'price', 'is_sold']
        

class GenreFrom(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        
class CategoryFrom(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']