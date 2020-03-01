import os

from erp_reloaded.settings.base import *  # noqa: F401
from erp_reloaded.settings.base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE

DEBUG = True
ALLOWED_HOSTS = []
TIME_ZONE = 'America/Los_Angeles'
SECRET_KEY = '1ey4!o_$yejljvfcc@z&nevnh37wnlvdpii$3#xbku69)!=s6e'

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE
INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'emails'
ADMINS = [('webmaster', 'martin@lehoux.net')]
DEFAULT_FROM_EMAIL = 'admin@erp-reloaded'
SERVER_EMAIL = 'admin@erp-reloaded'
EMAIL_SUBJECT_PREFIX = '[ERP Reloaded]'

# PROD:
#       logging.handlers.TimedRotatingFileHandler for everything
#       django.utils.log.AdminEmailHandler for errors
#       django.security handler
LOGGING = {
    'version': 1,
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
    },
    'handlers': {
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        # 'mail_admins': {
        #     'level': 'ERROR',
        #     'class': 'django.utils.log.AdminEmailHandler',
        # }
    },
    'loggers': {
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
        },
        'django': {
            'handlers': ['django.server'],
            'level': 'ERROR',
        },
    }
}
