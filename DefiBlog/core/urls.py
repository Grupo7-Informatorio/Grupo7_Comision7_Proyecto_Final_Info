
from django.urls import path, include
from core import views

urlpatterns = [
    path('',views.indexView, name = 'index'),
    path('integrantes/',views.integrantesView, name = 'integrantes'),
    path('publicaciones/', include('publicaciones.urls'))
]