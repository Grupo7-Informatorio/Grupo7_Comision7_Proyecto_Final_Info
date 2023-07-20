from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import usuario

class RegistroView(CreateView):
    model = usuario
    template_name = 'usuarios/registro.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('index')