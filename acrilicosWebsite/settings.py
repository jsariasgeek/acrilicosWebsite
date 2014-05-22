"""
Django settings for acrilicosWebsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'co(!nap+y*#ds#opoycsxv$tq#y$j0ow_2%)tl$o&*qg$rxov9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',    
    'imagekit',    
    'tinymce',    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Cache
)

ROOT_URLCONF = 'acrilicosWebsite.urls'

WSGI_APPLICATION = 'acrilicosWebsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'acrilicosWebsite.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/website/static/'
STATIC_ROOT = ''
MEDIA_ROOT = 'D:/projects-xero/acrilicos1000/acrilicosWebsite/website/media'
MEDIA_URL = '/website/'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'acrilicos1000website@gmail.com'
EMAIL_HOST_PASSWORD = 'Acri2014*-'
EMAIL_PORT = '587'


CACHES = {
    
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cacheacrilicos',
    }
}

# tinymce

# TINYMCE_JS_URL = '/website/tiny_mce/tiny_mce_src.js'
# TINYMCE_DEFAULT_CONFIG = {
#     'plugins': "table,spellchecker,paste,searchreplace",
#     'theme': "advanced",
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 10,
# }
# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True

# TINYMCE_JS_URL = 'http://xerocreatividad.com/tiny_mce/tiny_mce_src.js'
# TINYMCE_DEFAULT_CONFIG = {
#     'plugins': "table,spellchecker,paste,searchreplace",
#     'theme': "advanced",
# }
# TINYMCE_SPELLCHECKER = True
# TINYMCE_COMPRESSOR = True