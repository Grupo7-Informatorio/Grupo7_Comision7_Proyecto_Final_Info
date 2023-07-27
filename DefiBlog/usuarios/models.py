from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class usuario(AbstractUser):
    telefono = models.CharField(max_length=255, blank = True, null = True)
    domicilio = models.CharField(max_length=255, blank = True, null = True)
    imagen_perfil = models.ImageField(upload_to='imagenes_perfil', null=True, blank=True)
    es_colaborador = models.BooleanField(default = False)
    es_miembro = models.BooleanField(default = True)
    