from django.shortcuts import render, redirect
from .forms import RegisterForm, CustomLoginForm
from django.views import View
from django.contrib.auth import authenticate, login
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
    
class LoginView(View):
    template_name = 'login.html'
    form_class = CustomLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'home' with the name of your home page URL pattern
            else:
                # Add an error message for invalid credentials
                form.add_error(None, 'Invalid username or password.')
        return render(request, self.template_name, {'form': form})