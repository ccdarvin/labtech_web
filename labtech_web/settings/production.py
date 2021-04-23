from .base import *
import environ
env = environ.Env()

SECRET_KEY = env.db('SECRET_KEY')
ALLOWED_HOSTS = env.db('ALLOWED_HOSTS')
DEBUG = env.bool('DEBUG', True)

if 'DATABASE_URL' in env:
    DATABASES['default'] = env.db('DATABASE_URL')
    DATABASES['default']['ATOMIC_REQUESTS'] = True
    DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE', default=60)  # noqa F405

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = env.db('AWS_S3_REGION_NAME')
AWS_S3_ENDPOINT_URL = env.db('AWS_S3_ENDPOINT_URL')
AWS_ACCESS_KEY_ID = env.db('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env.db('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env.db('AWS_STORAGE_BUCKET_NAME') 

# try:
#     from .local import *
# except ImportError:
#     pass
#