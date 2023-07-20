from django.contrib.auth.forms import UserCreationForm
from .models import usuario
from django import forms
#clase que crea un formulario de registro

class RegisterForm(UserCreationForm):
    class Meta:
        model = usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'telefono', 'domicilio',] 
