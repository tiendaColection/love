from django import forms
from .models import Figurine, Genre, Category

class FigurineForm(forms.ModelForm):
    class Meta:
        model = Figurine
        fields = ['name', 'description', 'category', 'genre', 'imagen', 'price', 'is_sold']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre'}),
            'description':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Descripcion de la figura'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
        

class GenreFrom(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        
class CategoryFrom(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']