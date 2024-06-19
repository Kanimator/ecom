import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = False
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LANGUAGE_CODE = "en-us"
MEDIA_URL = "media/"
ROOT_URLCONF = "arkcomputing.urls"
SECRET_KEY = os.environ.get("KEY_ARK_COMPUTING", "")
STATIC_URL = "static/"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = "arkcomputing.wsgi.application"

CLIENT = {
    "NAME": "Ark Computing",
    "TITLE": "Ark Computing, LLC.",
    "ADDRESS": {
        "STREET": "",
        "CITY": "Cypress",
        "STATE": "TX",
        "ZIP": 77429,
    },
    "PHONE": {
        "MAIN": "",
        "OTHER": "",
    },
    "EMAIL": {
        "MAIN": "support@arkcomputing.tech",
        "SUPPORT": "support@arkcomputing.tech",
        "SALES": "sales@arkcomputing.tech",
        "NOREPLY": "no-reply@arkcomputing.tech",
    },
    "SOCIAL": {
        "FACEBOOK": "",
        "INSTAGRAM": "https://www.instagram.com/arkcomputing",
        "X": "",
        "TIKTOK": "https://www.tiktok.com/@arkcomputing",
    },
}

ALLOWED_HOSTS = [
    "arkcomputing.tech",
    "www.arkcomputing.tech",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "ecom.apps.EcomConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "postgresql": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PSQL_NAME", "postgres"),
        "USER": os.environ.get("PSQL_USER", "postgres"),
        "PASSWORD": os.environ.get("PSQL_PASS", ""),
        "HOST": os.environ.get("PSQL_HOST", "0.0.0.0"),
        "PORT": os.environ.get("PSQL_PORT", "5432"),
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
