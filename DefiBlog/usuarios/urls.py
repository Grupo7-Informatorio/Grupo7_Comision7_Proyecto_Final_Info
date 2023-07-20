from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from usuarios.views import RegistroView


app_name = 'usuarios'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'usuarios/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = '../login'), name = 'logout'),
    path('registro/', RegistroView.as_view(), name = 'registro' ),
]