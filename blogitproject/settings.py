"""
Django settings for blogitproject project.

Based on by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import posixpath
import psycopg2
from django.contrib.messages import constants as messages
from blogitproject.secret_key import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f73cacb9-77d5-4ce5-bb18-6eea203ae9bf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
INSTALLED_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'comments',
    'pages',
    'blogs',
    'profiles',
    'likes',
    'django_cleanup',
    'taggit',
    'easy_thumbnails',
    'widget_tweaks',
    'leads',
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogitproject.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],#ссылка на папку шаблонов
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

WSGI_APPLICATION = 'blogitproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow' #временная зона
USE_I18N = True
USE_L10N = True
USE_TZ = False #
DATE_INPUT_FORMATS=(
    '%d.%m.%Y', '%Y-%m-%d', '%d.%m.%y',# '25.10.2006', '25.10.2006', '25.10.06'
    '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y',# '25-10-2006', '25/10/2006', '25/10/06'
    '%d %b %Y',# '25 Oct 2006', 
    '%d %B %Y',# '25 October 2006', 
)
DATETIME_INPUT_FORMATS=(
    '%d.%m.%y %H:%M', '%d.%m.%y %H:%M:%S','%d.%m.%Y %H:%M', '%d.%m.%Y %H:%M:%S','%Y-%m-%d %H:%M:%S',
   '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d%H:%M',
  '%Y-%m-%d', '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M:%S.%f',
  '%m/%d/%Y %H:%M', '%m/%d/%Y', '%m/%d/%y %H:%M:%S',
 '%m/%d/%y %H:%M:%S.%f', 
 '%m/%d/%y %H:%M', '%m/%d/%y')
DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y HH:MM:SS'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'blogitproject/static')]

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_URL = '/media/'

DATABASES = {"default": {
        "ENGINE":"django.db.backends.postgresql",
        "NAME":"blogitdb",
        "USER":"blogituser",
        "PASSWORD":"blogituser",
        "HOST":"localhost",
        "PORT":"5433",
        }}
    

MESSAGE_TAGS = {
messages.INFO: 'success',
messages.ERROR: 'danger'
}

TAGGIT_CASE_INSENSITIVE = True