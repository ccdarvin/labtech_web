from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7_lse67x))co#it#yc&tcr8(bt-f9d_a8hy^$i@cjj54!_0t5c'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    'wagtail.contrib.styleguide',
]

try:
    from .local import *
except ImportError:
    pass
