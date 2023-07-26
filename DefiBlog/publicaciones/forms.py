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
        widgets = {
           'titulo' : forms.TextInput(attrs = {'placeholder' : 'Aca va el titulo', 'class' : 'form-control-lg'},),
           'post' : forms.TextInput(attrs = {'placeholder' : 'Aqui lo que quieras publicar', 'class' : 'form-control'},),
           'categoria' : forms.Select(attrs = {'class' : 'form-select', 'placeholder' : 'selecciona una categoria'})
           }
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']