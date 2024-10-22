from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Category, Figurine
from .forms import FigurineForm, GenreFrom, CategoryFrom
import logging

def index(request):
    ofertas = 120
    categories = Category.objects.all()
    figurines = Figurine.objects.all()
    return render(request,'index.html', {'categories': categories, 'figurines': figurines, 'ofertas': ofertas})

def category_detail(request, category_id):
    ofertas = 120
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    figurines = Figurine.objects.filter(category=category)
    return render(request, 'category_detail.html', {'categories': categories,'category': category, 'figurines': figurines, 'ofertas': ofertas})

def figurine_detail(request, pk):
    ofertas = 120
    categories = Category.objects.all()
    figurines = Figurine.objects.all()
    figurine = get_object_or_404(Figurine, pk=pk)
    return render(request, 'figurine_detail.html', {'categories': categories, 'figurines': figurines,'figurine': figurine, 'ofertas': ofertas})


def solicitud(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == '1981mayo23':  # Cambia 'tucontraseña' por la contraseña que desees
            return render(request, 'redirecion.html')
        else:
            return HttpResponse("Contraseña incorrecta.")
    return render (request, 'solicitud.html')

def subir_figura(request):
    if request.method == 'POST':
        formulario = FigurineForm(request.POST, request.FILES)
        try:
            if formulario.is_valid():
                formulario.save()
                return redirect('index')
        except Exception as e:
            # Aquí puedes manejar la excepción, por ejemplo, registrarla o mostrar un mensaje
            print(f"Ocurrió un error al guardar la figura: {e}")
            # Puedes agregar un mensaje de error al formulario si es necesario
            formulario.add_error(None, "Hubo un error al guardar la figura.")
    else:
        formulario = FigurineForm()
    
    return render(request, 'aniedir.html', {'formulario': formulario})

def subir_genere(request):
    if request.method == 'POST':
        formulario = GenreFrom(request.POST, request.FILES)
        if formulario.is_valid():
                formulario.save()
                return redirect('subir_genero')
    else:
        formulario = GenreFrom()
    return render(request, 'genero.html', {'formulario': formulario,})

def subir_Categorie(request):
    if request.method == 'POST':
        formulario = CategoryFrom(request.POST, request.FILES)
        if formulario.is_valid():
                formulario.save()
                return redirect('subir_categoria')
    else:
        formulario = CategoryFrom()
    return render(request, 'categoria.html', {'formulario': formulario,})