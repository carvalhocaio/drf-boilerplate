from .base import *  # noqa

from decouple import Csv, config
from dj_database_url import parse as db_url

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1", cast=Csv())

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": config(
        "DATABASE_URL",
        default="sqlite:///" + str(BASE_DIR / "db.sqlite3"),  # noqa: F405
        cast=db_url,
    )
}

REST_FRAMEWORK.update(  # noqa: F405
    {
        "TEST_REQUEST_DEFAULT_FORMAT": "json",
    }
)
