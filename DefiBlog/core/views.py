from publicaciones.models import Publicaciones
from django.views.generic import ListView
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
def indexView(request):
    posts = Publicaciones.objects.annotate(num_likes=Count('meGusta')).order_by('-num_likes')[:2]
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)
# view renderiza pagina publicaciones!
def publicacionesView(request):
    return render(request, 'publicaciones.html', {})
# view renderiza pagina integrantes!
def integrantesView(request):
    return render(request, 'integrantes.html', {})
# view renderiza pagina categorias!
def categoriasView(request):
    return render(request, 'categorias.html', {})
