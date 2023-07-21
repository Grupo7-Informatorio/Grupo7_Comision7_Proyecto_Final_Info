from django import forms
from .models import Publicaciones


class CrearPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria', 'titulo', 'post']
        labels = {
            'titulo': '',
            'post' : '',
            'categoria' : ''
        }