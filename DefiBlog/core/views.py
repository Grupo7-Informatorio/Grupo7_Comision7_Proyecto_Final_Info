from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, 'index.html', {})
# view renderiza pagina publicaciones!
def publicacionesView(request):
    return render(request, 'publicaciones.html', {})
# view renderiza pagina integrantes!
def integrantesView(request):
    return render(request, 'integrantes.html', {})
# view renderiza pagina categorias!
def categoriasView(request):
    return render(request, 'categorias.html', {})
