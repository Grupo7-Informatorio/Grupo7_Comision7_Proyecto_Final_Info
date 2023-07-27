from django.contrib.auth.forms import UserCreationForm
from .models import usuario
from django import forms
#clase que crea un formulario de registro

class RegisterForm(UserCreationForm):
    class Meta:
        model = usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'telefono', 'domicilio','imagen_perfil'] 
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter a password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'imagen_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
