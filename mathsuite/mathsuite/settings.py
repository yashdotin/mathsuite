from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ================
# SECURITY
# ================

# Use environment variable for secret key (Render will set this)
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-not-for-production")

DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
RENDER = os.environ.get("RENDER")
if RENDER:
    ALLOWED_HOSTS.append(os.environ.get("RENDER_EXTERNAL_HOSTNAME", ""))


# ================
# INSTALLED APPS
# ================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'calculator',
    'converter',
    'geometry',
    'visualizer',
]


# ================
# MIDDLEWARE
# ================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Whitenoise for static files on Render
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = 'mathsuite.urls'


# ================
# TEMPLATES
# ================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # YOUR global templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'mathsuite.wsgi.application'


# ================
# DATABASE
# ================

# Default: SQLite for local development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Render deployment: PostgreSQL
if RENDER:
    DATABASES = {
        "default": dj_database_url.config(
            default="postgresql://postgres:postgres@localhost/postgres",
            conn_max_age=600,
            ssl_require=False
        )
    }


# ================
# STATIC FILES
# ================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_ROOT = BASE_DIR / "staticfiles"

# Whitenoise settings
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ================
# DEFAULT PRIMARY KEY
# ================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
