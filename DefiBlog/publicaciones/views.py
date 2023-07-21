from django.shortcuts import render
from publicaciones.models import Publicaciones
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .forms import CrearPublicacionForm


# Create your views here.
class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'

    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        return consulta_anterior.order_by('-fecha')
    
class CrearPublicacion(CreateView):
    model = Publicaciones
    template_name = 'publicaciones/crear-publicacion.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
class EditarPublicacion(UpdateView):
    model = Publicaciones
    template_name = 'publicaciones/editar-publicacion.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
class EliminarPublicacion(DeleteView):
    model = Publicaciones
    template_name ='publicaciones/eliminar-publicacion.html'
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')