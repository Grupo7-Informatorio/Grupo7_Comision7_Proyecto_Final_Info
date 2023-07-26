from typing import Any, Dict
from django.shortcuts import render
from publicaciones.models import Publicaciones, Comentario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse
from .forms import CrearPublicacionForm, ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'

    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        return consulta_anterior.order_by('-fecha')
    




class CrearPublicacion(LoginRequiredMixin, CreateView):
    model = Publicaciones
    template_name = 'publicaciones/crear-publicacion.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
    def form_valid(self, form):
            f = form.save(commit=False)
            f.creador_id = self.request.user.id
            return super().form_valid(f)



class EditarPublicacion(LoginRequiredMixin, UpdateView):
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
    



class DetallePublicacion(DetailView):
    template_name = 'publicaciones/detalle-publicacion.html'
    model = Publicaciones
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentario_form'] = ComentarioForm()
        return context
    
    def post(self, request, *args, **kwargs):
        publicacion = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.creador_id = self.request.user.id
            comentario.post = publicacion
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)
        



class BorrarComentario(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'publicaciones/borrar-comentario.html'

    def get_success_url(self):
        return reverse('publicaciones:detalle-publicacion', args = [self.object.post.id])
    