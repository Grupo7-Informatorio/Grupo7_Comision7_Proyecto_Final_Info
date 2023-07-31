
from django.urls import path, include
from core import views

urlpatterns = [
    path('',views.indexView, name = 'index'),
    path('integrantes/',views.integrantesView, name = 'integrantes'),
    path('publicaciones/', include('publicaciones.urls')),
    path('categorias/', views.categoriasView, name = 'categorias'),
    path('login/', include('usuarios.urls')),
    path('contacto/', include('contacto.urls')) 
]