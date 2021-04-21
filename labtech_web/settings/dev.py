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

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'
AWS_S3_REGION_NAME = 'fra1'
AWS_S3_ENDPOINT_URL = 'https://fra1.digitaloceanspaces.com'
AWS_ACCESS_KEY_ID = 'L5VZ46Q7DOFAYPD2GTL4'
AWS_SECRET_ACCESS_KEY = 'Bf38wjXZFfiD2ciQD5c4/PwMrgM4mYeEYdaFV9kGkEg'
AWS_STORAGE_BUCKET_NAME = 'labtech-dev'

try:
    from .local import *
except ImportError:
    pass
