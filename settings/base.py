import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'mzocbzyilc=7-@4ss-_o_z40q$nglz-(^0v^(r^lr*(s8+r_te'

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tastypie',
    'sorl.thumbnail',
    'members',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'uadminpy.urls'
WSGI_APPLICATION = 'uadminpy.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = 'uploads'
MEDIA_URL = '/uploads/'

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'