# Grupo7_Comision7_Proyecto_Final_Info

En este proyecto nos proponemos crear un blog sobre DeFi.

Para poder utilizar esta aplicacion es necesario crear un archivo "local_settings.py" a lado de el archivo "settings.py" original.

El nuevo archivo "local_settings.py" debe contener lo siguiente:

```python
from .settings import *

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'NOMBRE_DE_LA_DB',
'USER': 'USUARIO_DE_LA_DB',
'PASSWORD': 'CONTRASEÑA_DE_LA_DB',
'HOST': 'localhost',
'PORT': '3306',
}
}
```
