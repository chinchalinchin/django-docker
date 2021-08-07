
import os, dotenv, datetime

from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
APP_ENV = str(os.environ.setdefault('APP_ENV', 'local')).strip()

if APP_ENV == 'local':
    dotenv.load_dotenv(os.path.join(os.path.join(PROJECT_DIR, 'env'),'runtime.env'))


SECRET_KEY = str(os.getenv('SECRET_KEY')).strip()
APPEND_SLASH=False

# SERVICE CONFIGURATION
APP_HOST = str(os.environ.setdefault('APP_HOST', 'localhost')).strip()
APP_PORT = str(os.environ.setdefault('APP_PORT', '8000')).strip()

if APP_ENV == 'local':
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }
    ALLOWED_HOSTS = [ '*' ]
elif APP_ENV == 'container':
    DEBUG = True
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': str(os.getenv('POSTGRES_HOST')).strip(),
        'NAME': str(os.getenv('POSTGRES_DB')).strip(),
        'USER': str(os.getenv('POSTGRES_USER')).strip(),
        'PASSWORD': str(os.getenv('POSTGRES_PASSWORD')).strip(),
        'PORT': str(os.getenv('POSTGRES_PORT')).strip()
        }
    }
    ALLOWED_HOSTS = [ '*' ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
LANGUAGE_CODE, TIME_ZONE = 'en-us', 'UTC'
USE_I18N, USEL10N, USE_TZ = True, True, True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
