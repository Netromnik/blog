from .base import *
from uuid import uuid4
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", str(uuid4()))

DEBUG = False
CSRF_TRUSTED_ORIGINS = ["localhost",]

ALLOWED_HOSTS = ["localhost",]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}

CSRF_COOKIE_AGE = 2620800

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', ''),
        'USER': os.environ.get('POSTGRES_USER', ''),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', ''),
        'TEST': {
            'NAME': 'test_database',
        },

    },
}

WAGTAILADMIN_BASE_URL = "http://localhost"

# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", '')
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", False)
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", '')
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", '')
