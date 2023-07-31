from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['asunto', 'mensaje']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': ''}),
        }