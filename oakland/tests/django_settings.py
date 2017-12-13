import os
import sys
import importlib

import dj_database_url

# django settings for tests
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgis://pupa:pupa@localhost/opencivicdata')
SECRET_KEY = 'test'
INSTALLED_APPS = ('django.contrib.contenttypes',
                  'opencivicdata.core.apps.BaseConfig',
                  'opencivicdata.legislative.apps.BaseConfig',
                  'pupa')

CACHE_DIR = os.path.join(os.getcwd(), 'tests/_cache')
SCRAPED_DATA_DIR = os.path.join(os.getcwd(), 'tests/_data')

MIDDLEWARE_CLASSES = ()

# Django settings
DEBUG = False
TEMPLATE_DEBUG = False

MIDDLEWARE_CLASSES = ()
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "%(asctime)s %(levelname)s %(name)s: %(message)s",
            'datefmt': '%H:%M:%S'
        }
    },
    'handlers': {
        'default': {'level': 'DEBUG',
                    'class': 'pupa.ext.ansistrm.ColorizingStreamHandler',
                    'formatter': 'standard'},
    },
    'loggers': {
        '': {
            'handlers': ['default'], 'level': 'DEBUG', 'propagate': True
        },
        'scrapelib': {
            'handlers': ['default'], 'level': 'INFO', 'propagate': False
        },
        'requests': {
            'handlers': ['default'], 'level': 'WARN', 'propagate': False
        },
        'boto': {
            'handlers': ['default'], 'level': 'WARN', 'propagate': False
        },
    },
}


DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
