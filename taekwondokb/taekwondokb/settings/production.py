from .base import * 
import dj_database_url

DEBUG = False

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600
    ),
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


AWS_S3_ACCESS_KEY_ID = os.getenv("AWS_KEY")
AWS_S3_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET")
AWS_STORAGE_BUCKET_NAME = "taekwondokb"
AWS_QUERYSTRING_AUTH = False
AWS_S3_ENDPOINT_URL = 'https://s3.tebi.io'