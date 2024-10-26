from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('figurine/<int:pk>/', views.figurine_detail, name='figurine_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('solicitud/', views.solicitud, name ='solicitud'),
    path('eliminar/', views.eliminar, name='eliminar'),
    path('eliminar-categoria/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('figuraslist/', views.lista_figuras, name='lista_figuras'),
    path('eliminar-figura/<int:pk>/', views.eliminar_figura, name='eliminar_figura'),
    path('subir-figura/', views.subir_figura, name='subir_figura'),
    path('subir-genero/', views.subir_genere, name='subir_genero'),
    path('subir-categoria/', views.subir_Categorie, name='subir_categoria'),
    
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)