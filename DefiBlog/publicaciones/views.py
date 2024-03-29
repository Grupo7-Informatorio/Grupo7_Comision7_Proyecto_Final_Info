from typing import Any, Dict
from django.shortcuts import redirect, get_object_or_404, render
from publicaciones.models import Publicaciones, Comentario, Categoria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse
from .forms import CrearPublicacionForm, ComentarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import SuperusuarioAutorMixin, ColaboradorMixin
from django.db.models import Count


# Create your views here.
class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()

        # Annotate the queryset with the number of likes for each post
        queryset = queryset.annotate(num_likes=Count('meGusta'))
        
        categoria_seleccionada = self.request.GET.get('categoria')
        queryset = queryset.order_by('-fecha')
        if categoria_seleccionada:
            queryset = queryset.filter(categoria = categoria_seleccionada)
    
        orden = self.request.GET.get('orderby')
        if orden:
            if orden == 'fecha_asc':
                queryset = queryset.order_by('fecha')
            elif orden == 'fecha_desc':
                queryset = queryset.order_by('-fecha')
            elif orden == 'alf_asc':
                queryset = queryset.order_by('titulo')
            elif orden == 'alf_desc':
                queryset = queryset.order_by('-titulo')
            elif orden == 'likes_asc':
                queryset = queryset.order_by('num_likes')
            elif orden == 'likes_desc':
                queryset = queryset.order_by('-num_likes')

        return queryset




class CrearPublicacion(ColaboradorMixin, LoginRequiredMixin, CreateView):
    model = Publicaciones
    template_name = 'publicaciones/crear-publicacion.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
    def form_valid(self, form):
            f = form.save(commit=False)
            f.creador_id = self.request.user.id
            return super().form_valid(f)



class EditarPublicacion(SuperusuarioAutorMixin, LoginRequiredMixin, UpdateView):
    model = Publicaciones
    template_name = 'publicaciones/editar-publicacion.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')


    
class EliminarPublicacion(SuperusuarioAutorMixin, LoginRequiredMixin, DeleteView):
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

        if not self.request.user.is_authenticated:
            return redirect('usuarios:login')

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
        



class BorrarComentario(SuperusuarioAutorMixin, LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'publicaciones/borrar-comentario.html'

    def get_success_url(self):
        return reverse('publicaciones:detalle-post', args = [self.object.post.id])
    



def me_gusta_view(request, pk):
     if request.method == "POST":
         publicacion_id = request.POST.get('publicacion_id')
         publicacion = get_object_or_404(Publicaciones, id = publicacion_id)
         usuario = request.user
         if publicacion.meGusta.filter(id=usuario.id).exists():
             publicacion.meGusta.remove(usuario)
         else:
             publicacion.meGusta.add(usuario)
   
     return redirect('publicaciones:detalle-post' , pk=publicacion_id)