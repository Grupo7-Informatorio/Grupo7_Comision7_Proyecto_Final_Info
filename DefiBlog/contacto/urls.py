from django.urls import path
from .views import ContactoView, mensaje_enviado
app_name = 'contacto'


urlpatterns = [
    path('enviar-mensaje/', ContactoView.as_view(), name='enviar-mensaje'),
    path('mensaje-enviado/', mensaje_enviado, name='mensaje-enviado')
]