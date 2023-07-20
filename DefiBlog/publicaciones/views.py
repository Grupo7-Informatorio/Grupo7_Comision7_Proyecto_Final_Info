from django.shortcuts import render
from publicaciones.models import Publicaciones
from django.views.generic import ListView

# Create your views here.
class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'

    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        return consulta_anterior.order_by('fecha')