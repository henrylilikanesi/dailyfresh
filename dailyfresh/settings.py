"""
Django settings for dailyfresh project.

Generated by 'django-admin startproject' using Django 2.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h1&6xari8b33b)w&tv_rjsw^-+)(ts7dc%7a&j_1mclad#+&cv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',  # Rich text editor
    # 'haystack',  # Full text retrieval framework
    'user',
    'goods',
    'order',
    'cart',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dailyfresh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dailyfresh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dailyfresh',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库密码
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# the model class of Django authentication system
AUTH_USER_MODEL = 'user.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# STATIC_ROOT = '/var/www/html/Django2_dailyfresh/static'

# The rich text editor configuration
# https://django-tinymce.readthedocs.io/en/latest/installation.html

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}

# QQ Email for django config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.outlook.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'xxxx@qq.com'  # 发送邮件的邮箱
EMAIL_HOST_PASSWORD = 'xxxx'  # qq邮箱授权码
# EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)
EMAIL_FROM = '天天生鲜<XXXXX@qq.com>'  # EMAIL_FROM 和 EMAIL_HOST_USER必须一样

# django-redis cache configuration
# https://django-redis-chs.readthedocs.io/zh_CN/latest/

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.116.134:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# The configuration of the session
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Users center under the condition of the login to access
LOGIN_URL = '/user/login'

# Set the django file storage classes
DEFAULT_FILE_STORAGE = 'utils.fdfs.storage.FDFSStorage'
# Set fastdfs using the client of conf file path
# FDFS_CLIENT_CONF = '../utils/fdfs/client_deploy.conf'
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fdfs/client_deploy.conf')
# Set IP:port

FDFS_STORAGE_URL = 'http://ip:port'  # fdfs服务器的ip和端口，注意端口是nginx的端口

# haystack configure
HAYSTACK_CONNECTIONS = {
    'default': {
        # use whoosh engine
        # 'ENGINE': 'haystack.backends.whoosh_cnbackend.WhooshEngine£
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # Index file path
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

# CURD automatically generate the index
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 支付宝沙箱APP_ID
ALIPAY_APP_ID = '沙箱app id'

# 支付宝网站回调url地址
ALIPAY_APP_NOTIFY_URL = None

# 支付宝同步return_url地址
ALIPAY_APP_RETURN_URL = 'http://127.0.0.1:8000/order/check'

# 网站私钥文件路径
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'apps/order/app_private_key.pem')

# 支付宝公钥文件路径
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'apps/order/alipay_public_key.pem')

# 支付宝支付的开发模式
ALIPAY_DEBUG = True

# 支付宝沙箱支付网关地址
ALIPAY_GATEWAY_URL = 'https://openapi.alipaydev.com/gateway.do?'
