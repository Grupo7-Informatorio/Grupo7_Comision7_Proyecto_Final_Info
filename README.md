# Grupo7_Comision7_Proyecto_Final_Info

# DescentraBlog

_Blog sobre finanzas descentralizadas creado en Django ._

## Comenzando 🚀

_Para obtener una copia del proyecto funcionando en tu PC de manera local para propósitos de desarrollo y pruebas, seguí las instrucciones_


### Pre-requisitos 📋

Python 3.10 o superior https://www.python.org/downloads/

Pip


_Antes de iniciar, es recomendable generar un entorno virtual de trabajo donde instalaremos las dependencias necesarias para que el proyecto funcione. Para ello, abrimos el CMD y nos dirigimos a la carpeta donde queremos guardar el entorno virtual y ejecutamos el siguiente comando:_


```
virtualenv nombre-entorno

```
_Una vez creado es necesario activarlo para ello ejecutamos la siguiente linea (en Windows):_


```
nombre_del_entorno\Scripts\activate.bat

```

_Ya contamos con un entorno virtual activado en el cual podemos instalar todas las dependencias para correr nuestro proyecto._


_Luego, con el entorno activado, nos dirigimos a la carpeta donde se encuentra el archivo requirements.txt y ejecutamos el siguiente comando en la consola._

```
pip install -r requirements.txt

```
_Este comando instalará en nuestro entorno todo lo necesario para que el proyecto funcione correctamente._

### SETTINGS 🔧

Luego tenes que crear un archivo de configuraciones en la carpeta DefiBlog/ y llamarlo "local_settings.py", donde debes indicar las credenciales de tu base de datos como se muestra a continuacion.

```
from .base import *

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static"),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'databaseName',
        'USER': 'databaseUser',
        'PASSWORD': 'databasePassword',
        'HOST': 'localhost',
        'PORT': 'portNumber',
    }
}

```

Tambien será necesario modificar en settings.py que DEBUG sea True

```
DEBUG= True
```

Y modificar manage.py para que settings sea local_settings.py

```
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DefiBlog.local_settings')
```


## Construido con 🛠️

_Las herramientas utilizadas para el desarrollo fueron:_

* [Django](https://www.djangoproject.com/) Framework web
* [Python](https://www.python.org/) Del lado del servidor (backend)
* [Bootstrap](https://getbootstrap.com/) Framework web para el desarrollo frontend (HTML, CSS, JavaScript)
* [MySql](https://www.mysql.com/) - Sistema de gestión de bases de datos.


## Autor ✒️

_Proyecto desarrollado por:_ 


- AGUSTIN RODRIGUEZ

- ALBERTO FABIAN BASTIANI

- ELIAS BRAZANOVICH

- MAURICIO STALCAR

- NICOLAS MIGUEL ARREJIN

- VALERIA MARGARITA NUÑEZ



También puedes mirar la lista de todos los [contribuyentes](https://github.com/Grupo7-Informatorio/Grupo7_Comision7_Proyecto_Final_Info/graphs/contributors) quienes han participado en este proyecto. 




---
