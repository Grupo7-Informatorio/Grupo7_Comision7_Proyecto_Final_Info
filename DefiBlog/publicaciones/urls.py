from django.urls import path
from publicaciones import views

app_name = 'publicaciones'
urlpatterns = [
    path('publicaciones/',views.VerPublicaciones.as_view(), name = 'publicaciones'),
    path('crear-publicacion/', views.CrearPublicacion.as_view(), name='crear-publicacion'),
    path('editar-publicacion/<int:pk>', views.EditarPublicacion.as_view(), name='editar-publicacion'),
    path('eliminar-publicacion/<int:pk>', views.EliminarPublicacion.as_view(), name = 'eliminar-publicacion'),
    path('detalle-post/<int:pk>', views.DetallePublicacion.as_view(), name='detalle-post'),
    path('borrar-comentario/<int:pk>', views.BorrarComentario.as_view(), name='borrar-comentario'),
    path('detalle-post/me_gusta/<int:pk>', views.me_gusta_view, name='me-gusta'),
]