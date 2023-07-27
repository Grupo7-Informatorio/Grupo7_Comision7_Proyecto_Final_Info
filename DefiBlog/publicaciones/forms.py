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
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'post': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your post here'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']