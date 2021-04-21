from .base import *

SECRET_KEY = '7_lse67x))co#it#yc&tcr8(bt-f9d_a8hy^$i@cjj54!_0t5c'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'labtech-ai',
        'USER': 'labtech-ai',
        'PASSWORD': 'ai ! 683-fd$D',
        'HOST': 'labtech-ai.database.windows.net',
        'PORT': '1433',

        'OPTIONS': {
            'driver': 'ODBC Driver 13 for SQL Server',
        },
    },
}

#Serve;Database=labtech-ai;Uid=labtech-ai;Pwd={your_password_here};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
DATABASE_CONNECTION_POOLING = False

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = 'labtechai'
AZURE_ACCOUNT_KEY = 'j04o8xIO7wC0xGFllJ40872ZTU6Ii+N7lpI6OxsUIMY3IQ5w03CQRXRtKFduvJPKAk8WOcCfNHwnXWmbEYamkA=='
#AZURE_CUSTOM_DOMAIN='cdn.labtech.ai'
AZURE_CONTAINER = 'media'

try:
    from .local import *
except ImportError:
    pass
