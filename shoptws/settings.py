from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




SECRET_KEY = 'django-insecure-v*u)y#2i+ou^$d^7_mb6xjfb%ao1$ow&xp5s2(b#2hz739$$6@'
STRIPE_API_KEY_PUBLISHABLE="pk_test_51JujYiCKMB1QFzwpoFJFb5oHQzgBFRb0I77QjdiBL9Z1gGFede4mwJuAuCxSRt05OzGelaqte1FEjfE0aaAbNDZV00V4XEqQE9"
STRIPE_API_KEY_HIDDEN="sk_test_51JujYiCKMB1QFzwpoFfeIeTPqJeXCEQgTDGX5aOp4gUOFSr4Fxsz5au7wL2N7xX8iDAWMXhhBiqGHW21sBo18IPJ00WVtY8VRs"


DEBUG = True

ALLOWED_HOSTS = []


SESSION_COOKIE_AGE = 86400
CART_SESSION_ID='cart'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'tailwind',
    'theme',
    
    'apps.core',
    'apps.store',
    'apps.cart',
    'apps.coupon',
    'apps.accounts',
    'apps.order',
]
#accounts
LOGIN_URL='login'
LOGIN_REDIRECT_URL='cart'
LOGOUT_REDIRECT_URL='frontpage'
#


# Email
EMAIL_HOST="localhost"
EMAIL_PORT="1025"

#


#tailwind

TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = '/usr/bin/npm'

#
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shoptws.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.store.context_processors.menu_categories',
                'apps.cart.context_processors.cart',
                
                
            ],
        },
    },
]

WSGI_APPLICATION = 'shoptws.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = 'media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
