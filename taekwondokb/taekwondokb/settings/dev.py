from .base import *
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

STATIC_ROOT = ''

STATICFILES_DIRS=[
    BASE_DIR / 'static'
]
