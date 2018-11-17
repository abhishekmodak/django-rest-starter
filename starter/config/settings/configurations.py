
# Complete configuration file
# Want any change make here
# Don't touch base.py, dev.py or prod.py unnecessarily

SETUP = "DEVELOPMENT"   #DEVELOPMENT/PRODUCTION

AUTH_USER_MODEL = "accounts.User"

REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
                    'rest_framework.authentication.TokenAuthentication',
                    'rest_framework.authentication.SessionAuthentication'
                ),
        'DEFAULT_FILTER_BACKENDS': (
                    'django_filters.rest_framework.DjangoFilterBackend',
                    'rest_framework.filters.SearchFilter',
                ),
        'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
        'EXCEPTION_HANDLER': 'factory.custom_exception.custom_exception_handler',
    }



EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'sendgrid_username'
EMAIL_HOST_PASSWORD = 'sendgrid_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SENDER = 'sender_email'