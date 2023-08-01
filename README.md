# Grupo7_Comision7_Proyecto_Final_Info

En este proyecto nos proponemos crear un blog sobre DeFi.

Este proyecto es realizado por:

- AGUSTIN RODRIGUEZ

- ALBERTO FABIAN BASTIANI

- ELIAS BRAZANOVICH

- MAURICIO STALCAR

- NICOLAS MIGUEL ARREJIN

- VALERIA MARGARITA NUÑEZ

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

Luego tenes que crear un archivo de configuraciones en la carpeta DefiBlog/ y llamarlo "local.py", donde debes indicar las credenciales de tu base de datos como se muestra a continuacion.

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


## Construido con 🛠️

_Las herramientas utilizadas para el desarrollo fueron:_

* [Django](https://www.djangoproject.com/) Framework web
* [Python](https://www.python.org/) Del lado del servidor (backend)
* [Bootstrap](https://getbootstrap.com/) Framework web para el desarrollo frontend (HTML, CSS, JavaScript)
* [MySql](https://www.mysql.com/) - Sistema de gestión de bases de datos.


## Autor ✒️

_Proyecto desarrollado por:_ 


**INTEGRANTE 1**
**INTEGRANTE 2**
**INTEGRANTE 3**

 



También puedes mirar la lista de todos los [contribuyentes](link-al-area-de-contribuyentes) quienes han participado en este proyecto. 




---
