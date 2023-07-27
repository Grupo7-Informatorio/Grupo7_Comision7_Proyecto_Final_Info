from django.contrib.auth.mixins import UserPassesTestMixin

class SuperusuarioAutorMixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        obj = self.get_object()

        if hasattr(obj, 'creador'):
            return usuario == obj.creador or usuario.is_superuser
    
        if hasattr(obj,'post.creador'):
            return usuario == obj.creador or usuario.is_superuser or usuario == obj.post.creador
    
class ColaboradorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.es_colaborador or self.request.user.is_superuser