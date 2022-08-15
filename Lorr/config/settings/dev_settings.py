from .base_settings import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-45fl!!k_=$lj_#)@je@e7pcldx)b*-0%k4=#i$%y^oa$mu_1xz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}