from os import environ as env
from pathlib import Path

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ECOM_ENCRYPTION_KEY = env.get("ECOM_ENCRYPTION_KEY", "")
INTERNAL_IPS = ["127.0.0.1"]
LANGUAGE_CODE = "en-us"
MEDIA_URL = "media/"
ROOT_URLCONF = "src.urls"
SECRET_KEY = "django-insecure-9f2wz(#_vn_c6)h&0-7+(o6eqij(i6s@#4sp_rz_5a4%$-*uj9"
STATIC_URL = "/static/"
TAILWIND_APP_NAME = "theme"
TIME_ZONE = "America/Chicago"
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = "src.wsgi.application"

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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "postgresql": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.get("PSQL_NAME", "postgres"),
        "USER": env.get("PSQL_USER", "postgres"),
        "PASSWORD": env.get("PSQL_PASS", ""),
        "HOST": env.get("PSQL_HOST", "0.0.0.0"),
        "PORT": env.get("PSQL_PORT", "5432"),
    },
}

ECOM_USERDATA = {
    "NAME": "Crimson Slate",
    "ADDRESS": {
        "STREET": "123 Main St",
        "CITY": "Houston",
        "STATE": "TX",
        "ZIP": "77065",
    },
    "PHONE": {
        "MAIN": "+15555555555",
        "SUPPORT": "+15555555555",
        "SALES": "+15555555555",
    },
}

INSTALLED_APPS = [
    "ecom.apps.EcomConfig",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_htmx",
    "tailwind",
    "theme",
    "django_browser_reload",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.admindocs.middleware.XViewMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
    "bucket": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}

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
