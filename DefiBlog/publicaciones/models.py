from django.db import models
from usuarios.models import usuario


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre 

class Publicaciones(models.Model):
    fecha = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now=True)
    titulo = models.CharField(max_length = 255)
    post = models.TextField()
    imagen_post = models.ImageField(upload_to='imagenes_post', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='posteos', null= True)
    creador = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='posteos_usario')
    meGusta = models.ManyToManyField(usuario, related_name='publicaciones_gustadas', blank=True)

    def __str__(self):
        return self.titulo + '-' + self.creador.username
    
class Comentario(models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Publicaciones, on_delete=models.CASCADE, related_name='comentarios')
    creador = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='comentarios')
    meGusta = models.ManyToManyField(usuario, related_name='comentarios_gustados', blank=True)

    def __str__(self):
        return self.post.titulo + '-' + self.creador.username