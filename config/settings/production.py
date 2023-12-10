from .base import *  # noqa

from decouple import Csv, config
from dj_database_url import parse as db_url

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

CORS_ALLOWED_ORIGINS = []

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {"default": config("DATABASE_URL", cast=db_url)}

REST_FRAMEWORK.update(  # noqa: F405
    {
        "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    }
)
