from django import forms
from .models import Publicaciones, Comentario


class CrearPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria', 'titulo', 'post']
        labels = {
            'titulo': '',
            'post' : '',
            'categoria' : ''
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']