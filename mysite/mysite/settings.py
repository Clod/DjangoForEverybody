"""
Django settings.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Used for a default title
APP_NAME = 'ClodList' 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*******************************************'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Extensions needed.
    'django_extensions',
    'crispy_forms',
    'crispy_bootstrap5',
    'rest_framework',
    'social_django',
    'taggit',
    
    # Home application (Sort of a launchpad and landing page)
    'home.apps.HomeConfig',

    # Applications
    'ads.apps.AdsConfig',
    'autos.apps.AutosConfig',
    'cats.apps.CatsConfig',
    'hello.apps.HelloConfig',
    'polls.apps.PollsConfig',

]

# When we get to tagging

# When we get to crispy forms :)
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

TAGGIT_CASE_INSENSITIVE = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',   # Add
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS: This is an empty list, which means Django will not look 
        # for templates in any specific directories outside of the app directories.
        'DIRS': [],
        # APP_DIRS: This is set to True, which means Django will look for templates 
        # in the templates directory of each installed app.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processors.settings',      # Add
                'social_django.context_processors.backends',  # Add
                'social_django.context_processors.login_redirect', # Add
            ],
        },
    },
]

# WSGI_APPLICATION = 'dj4e-samples.wsgi.application'
WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'Clod$ads',
#         'USER': 'Clod',
#         'PASSWORD': 'PataDeCabra1962',
#         'HOST': 'Clod.mysql.pythonanywhere-services.com',
#          'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

# Add the settings below

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

# Configure the social login if needed

# Django's authentication views use a default template location for rendering the login 
# page. By default, Django looks for templates in the registration directory within each 
# app's templates directory. In this case, Django will look 
# for the login template at home/templates/registration/login.html.

try:
    from . import github_settings           # mysite/mysite/github_settings.py
    SOCIAL_AUTH_GITHUB_KEY = github_settings.SOCIAL_AUTH_GITHUB_KEY
    SOCIAL_AUTH_GITHUB_SECRET = github_settings.SOCIAL_AUTH_GITHUB_SECRET
except:
    print('When you want to use social login, please see dj4e-samples/github_settings-dist.py')


# https://python-social-auth.readthedocs.io/en/latest/configuration/django.html#authentication-backends
# https://simpleisbetterthancomplex.com/tutorial/2016/10/24/how-to-add-social-login-to-django.html
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'

# Don't set default LOGIN_URL - let django.contrib.auth set it when it is loaded
# LOGIN_URL = '/accounts/login'

# Needed for 3.2 and later
# https://stackoverflow.com/questions/67783120/warning-auto-created-primary-key-used-when-not-defining-a-primary-key-type-by
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# https://coderwall.com/p/uzhyca/quickly-setup-sql-query-logging-django
# https://stackoverflow.com/questions/12027545/determine-if-django-is-running-under-the-development-server

'''  
# Leave off for now
import sys
if (len(sys.argv) >= 2 and sys.argv[1] == 'runserver'):
    print('Running locally')
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            }
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        }
    }
'''
