from django.urls import path
from core import views

app_name = 'publicaciones'
urlpatterns = [
    path('publicaciones/',views.publicacionesView, name = 'publicaciones')
]