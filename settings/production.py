from settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False

import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

HEROKU_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATICFILES_DIRS = (
    os.path.join(HEROKU_BASE_DIR, 'static'),
)