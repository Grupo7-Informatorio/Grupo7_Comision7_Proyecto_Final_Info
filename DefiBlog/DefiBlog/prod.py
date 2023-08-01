from .settings import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mawryshub$default',
        'USER': 'mawryshub',
        'PASSWORD': 'AdminDB99',
        'HOST': 'mawryshub.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}