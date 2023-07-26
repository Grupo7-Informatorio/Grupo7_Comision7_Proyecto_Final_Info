from typing import Optional
from django.contrib.auth.mixins import UserPassesTestMixin

class SuperusuarioAutorMixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        obj = self.get_object()

        return usuario == obj.creador or usuario.is_superuser