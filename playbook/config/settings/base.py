"""
Base Django settings for playbook project and global variables.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import logging.config
from os.path import abspath, basename, dirname, join, normpath
from os import listdir
from sys import path

############################################################################################################################################################
# Path configuration
############################################################################################################################################################

# Absolute path of the config directory
CONFIG_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the django repo directory
DJANGO_ROOT = dirname(CONFIG_ROOT)

# Absolute filesystem path to the project directory
PROJECT_ROOT = dirname(CONFIG_ROOT)

# Project name
PROJECT_NAME = basename(PROJECT_ROOT).capitalize()

# Project folder
PROJECT_FOLDER = basename(PROJECT_ROOT)

# Project domain TODO
PROJECT_DOMAIN = '%s.com' % PROJECT_NAME.lower()

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(CONFIG_ROOT)

############################################################################################################################################################
# Email configuration
############################################################################################################################################################

EMAIL_USE_TLS = True
EMAIL_HOST = os.getenv('SMTP_SERVER')
EMAIL_HOST_USER = os.getenv('SMTP_USER')
EMAIL_HOST_PASSWORD = os.getenv('SMTP_PASSWORD')
EMAIL_PORT = os.getenv('SMTP_PORT')
EMAIL_RECIPIENT_LIST = os.getenv('EMAIL_HOST_USER')
EMAIL_SUBJECT_PREFIX = '[%s]' % PROJECT_NAME


#LOGGING_CONFIG = None

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#CORE_PROJECT_DIR = os.path.join(BASE_DIR, 'playbook/core')

#logging.config.fileConfig(os.path.join(CORE_PROJECT_DIR, 'logging.ini'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

################################################################################
# Security and Debug configuraiton
################################################################################

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = '-ccj-m$@5h9z$t%+9zq6z$y@s%e9+kapdy^ozt4k^lfvpq)bxm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

################################################################################
# Application Configuration
################################################################################

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
)

PROJECT_APPS = (
    'apps.shared',
    'apps.backlog',
    'apps.accounts',
)

EXTENSION_APPS = (
    'django_extensions',
)

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS + EXTENSION_APPS

################################################################################
# Middleware Configuration
################################################################################

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'config.urls'


################################################################################
# Template Configuration
################################################################################

def template_folder_paths(app):
    """
    This method is able to get a namespace and transforms it into a normalized
    string with a template path. For example, 'app.google' will return ['app',
    'google'].
    """
    normalized_app = app.split('.') + ['templates']
    return normpath(join(PROJECT_ROOT, *normalized_app))

PROJECT_APP_TEMPLATES = [template_folder_paths(app) for app in PROJECT_APPS]
BASE_TEMPLATES = [normpath(join(PROJECT_ROOT, 'core', 'templates'))]
EXTENSION_TEMPLATES = [normpath(join(PROJECT_ROOT, 'extensions', 'templates'))]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_APP_TEMPLATES + BASE_TEMPLATES + EXTENSION_TEMPLATES,
        'APP_DIRS': True, #TODO
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

################################################################################
# Login Configuration
################################################################################

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = 'index'

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
#LOGIN_URL = '/login/'

# https://docs.djangoproject.com/en/dev/ref/settings/#logout-url
#LOGOUT_URL = '/logout/'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME':     os.getenv('PLAYBOOK_DB_NAME'),
    'USER':     os.getenv('PLAYBOOK_DB_USER'),
    'PASSWORD': os.getenv('PLAYBOOK_DB_PASSWORD'),
    'HOST':     os.getenv('PLAYBOOK_DB_HOST'),
    'PORT':     os.getenv('PLAYBOOK_DB_PORT'),
    }
}

################################################################################
# Miscellaneous configuration
################################################################################

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
ROOT_URLCONF = 'config.urls'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'

USE_I18N = True
USE_L10N = True
USE_TZ = True

WSGI_APPLICATION = 'config.wsgi.application'
SESSION_COOKIE_AGE = 10 * 60  # 10 minutes


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

INTERNAL_IPS = ('127.0.0.1',)

############################################################################################################################################################
# Github configuration
############################################################################################################################################################

GITHUB_OWNER = os.getenv('PLAYBOOK_GITHUB_OWNER')
GITHUB_TOKEN = os.getenv('PLAYBOOK_GITHUB_TOKEN')
GITHUB_WEBHOOK_SECRET = os.getenv('PLAYBOOK_GITHUB_WEBHOOK_SECRET')
