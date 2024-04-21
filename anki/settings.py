"""
Django settings for anki project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# os.getnev() - функция для получения переменных окружения
# вернет None, если переменной нет и значение переменной, если она есть
# Если будет DEBUG=True, то DEBUG = True, иначе False
# Тогда будет установлено значение  DEBUG = 'True' == 'True'
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ["82.97.247.78", "vladimirmonin-django-329-d5fd.twc1.net", "127.0.0.1"]
CSRF_TRUSTED_ORIGINS = ['https://vladimirmonin-django-329-d5fd.twc1.net']



INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

# Application definition

INSTALLED_APPS = [
    'django_extensions',  # Подключение django-extensions Для shell_plus
    'debug_toolbar',  # Подключение debug_toolbar
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cards.apps.CardsConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'anki.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Папка с шаблонами
        ],
        'APP_DIRS': True,  # Поиск шаблонов внутри приложений
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.get_menu',
            ],
        },
    },
]

WSGI_APPLICATION = 'anki.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'lesson_47.db',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'  # Язык в админке
TIME_ZONE = 'UTC'  # Часовой пояс для всего проекта
USE_I18N = True
USE_TZ = True  # Python pytz - библиотека для работы с часовыми поясами
STATIC_URL = 'static/'


LOGIN_URL = 'users:login'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',

    }
}


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Стандартный бекенд для аутентификации по username
    'users.authentication.EmailAuthBackend',      # Наш кастомный бекенд для аутентификации по email
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'