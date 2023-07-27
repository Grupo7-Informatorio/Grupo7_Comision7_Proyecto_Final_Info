from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import RegistroView, LoginView


app_name = 'usuarios'

urlpatterns = [
    path('', LoginView.as_view(template_name = 'usuarios/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = '../login'), name = 'logout'),
    path('registro/', RegistroView.as_view(), name = 'registro' ),
]