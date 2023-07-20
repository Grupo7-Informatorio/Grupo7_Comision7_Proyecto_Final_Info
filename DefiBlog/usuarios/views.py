from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import usuario

class RegistroView(CreateView):
    model = usuario
    template_name = 'usuarios/registro.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('index')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response