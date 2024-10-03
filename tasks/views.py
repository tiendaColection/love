from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Category, Figurine

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

