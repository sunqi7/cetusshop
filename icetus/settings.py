"""
Django settings for imycart project.

Generated by 'django-admin startproject' using Django 1.8.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(3lj3*1&2q)mbldx-pqj3mf2yjfk)ae_*+tsykzdwrf1gnrkf)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SESSION_COOKIE_AGE = 1800
#SESSION_COOKIE_AGE = 10
#默认的session过期时间，默认是1800秒

SITE_ID = '1'

LOGIN_URL = '/user/login/'

# Application definition

INSTALLED_APPS = (
	#'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.sites',
	'shopcart',
	'captcha',
	'paypal.standard.ipn',
	'django_comments', 
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.locale.LocaleMiddleware',#使用i18n需要的中间件
    'django.contrib.auth.middleware.AuthenticationMiddleware',
	'shopcart.my_login_check.MyLoginCheckMiddleware',#添加自定义中间件，检查用户是否被冻结
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'icetus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'icetus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cassie',
        'USER': 'cassie',
        'PASSWORD': 'cassie',
        #'HOST':'192.168.137.129',
		'HOST':'localhost',
		#'HOST':'www.imycart.com',
        'PORT':'3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
#TIME_ZONE = 'Asia/Shanghai'

USE_I18N = False
#梳子网站不启用中文

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'shopcart.MyUser'


#加入这一段的时候，需要注意下面指定的日志目录，必须先建好，不然会报错
LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'filters': {
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		},
	},
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'filters': ['require_debug_true'],
			'class': 'logging.StreamHandler',
			'formatter': 'simple'
		},
		'mail_admins': {
			'level': 'ERROR',
			'class': 'django.utils.log.AdminEmailHandler',
		},
		'default': {
			'level':'DEBUG',
			'class':'logging.handlers.RotatingFileHandler',
			'filename': os.path.join('logs/','all.log'),
			'maxBytes': 1024*1024*5, # 5 MB
			'backupCount': 5,
			'formatter':'simple',
		},
	},
	'loggers': {
		#'django.db.backends': {
        #    'handlers': ['console'],
        #    'propagate': True,
        #    'level':'DEBUG',
        #},
		'django': {
			'handlers': ['console'],
			'propagate': True,
		},
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': False,
		},
		'icetus.shopcart': {
			'handlers': ['console', 'default'],
			'level': 'DEBUG',
		}
	}
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "shopcart/static"),)

MEDIA_URL='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

#STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), os.path.join(BASE_DIR, "shopcart/static"),)