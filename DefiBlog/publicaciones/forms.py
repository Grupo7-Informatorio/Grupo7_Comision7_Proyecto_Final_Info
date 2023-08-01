from django import forms
from .models import Publicaciones, Comentario


class CrearPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['categoria', 'titulo', 'post', 'imagen_post']
        labels = {
            'titulo': '',
            'post' : '',
            'categoria' : '',
            'imagen para el post':''
        }
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'post': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escriba su post aqui'}),
            'imagen_post': forms.ClearableFileInput(attrs={'class': 'form-control'}), 
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe un comentario'}),
        }