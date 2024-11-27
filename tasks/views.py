from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Category, Figurine
from .forms import FigurineForm, GenreFrom, CategoryFrom

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

def eliminar(request):
    categorias = Category.objects.all()
    return render(request, 'categoriaDelete.html', {'categorias': categorias})

def lista_figuras(request):
    try:
        figuras = Figurine.objects.all()
    except Figurine.DoesNotExist:
        figuras = []
        print("ocurrio un error a listar las figuras")# Puedes agregar un mensaje de error o manejarlo de otra manera
        figuras.add_error(None, "Hubo un error al guardar la figura.")
    return render(request, 'listarfigura.html', {'figuras': figuras})

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

def editar_figura(request, pk):
    figura = get_object_or_404(Figurine, pk=pk)
    if request.method == 'POST':
        form = FigurineForm(request.POST, request.FILES, instance=figura)
        if form.is_valid():
            form.save()
            return redirect('lista_figuras')  # Redirige a la lista de figuras o a donde prefieras
    else:
        form = FigurineForm(instance=figura)
    return render(request, 'editarFigura.html', {'form': form})

def eliminar_categoria(request, pk):
    if request.method == 'POST':
        categoria = get_object_or_404(Category, pk=pk)
        categoria.delete()
        return redirect('eliminar')
    
def eliminar_figura(request, pk):
    if request.method == 'POST':
        figura = get_object_or_404(Figurine, pk=pk)
        figura.delete()
        return redirect('lista_figuras')