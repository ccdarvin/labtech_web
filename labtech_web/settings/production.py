from .base import *
import environ
env = environ.Env()

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
DEBUG = env.bool('DEBUG', True)

if 'DATABASE_URL' in env:
    DATABASES['default'] = env.db('DATABASE_URL')
    DATABASES['default']['ATOMIC_REQUESTS'] = True
    DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE', default=60)  # noqa F405

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
AWS_S3_ENDPOINT_URL = env('AWS_S3_ENDPOINT_URL')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME') 
AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN') 
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'

# try:
#     from .local import *
# except ImportError:
#     pass
#