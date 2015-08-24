"""
Django settings for omc project.

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
SECRET_KEY = '0dedy!=^8f9=@+w*vcta%us2u3l!!)#@g3l8qrltfiba^q$=-o'

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
    #'xadmin',
    #'crispy_forms',
    #'reversion',
    'ops',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'omc.urls'

WSGI_APPLICATION = 'omc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
DATABASES = {
 'default': {
 'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
 'NAME': 'omc', # Or path to database file if using sqlite3.
 # The following settings are not used with sqlite3:
 'USER': 'root',
 'PASSWORD': 'root',
 'HOST': '127.0.0.1', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
 'PORT': '3306', # Set to empty string for default.
 }
 }


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
STATICFILES_DIRS = (
    'static',
)

MEDIA_URL = '/static/media/'
MEDIA_ROOT = '/static/media/'

DOCUMENT_URL = '/uploads/'
DOCUMENT_ROOT = '/uploads/'



SALT_API = {"url": "http://127.0.0.1:8888/",
            "user": "saltapi",
            "password": "saltapi"
            }

# salt result

RETURNS_MYSQL = {
    'salt': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'salt',    #database name
        'USER': 'root',   #username
        'PASSWORD': 'root', #passwd
        'HOST': '127.0.0.1', #localhost
        'PORT': '3306', #mysql port
    }
}
# salt-api setting
SALT_API = {
        'url' : 'http://127.0.0.1:8888/',
        'user' : 'saltapi',
        'password' : 'saltapi'
        }
        
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
                'format': '%(asctiome)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d%(message)s'
                }
    },
    
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
