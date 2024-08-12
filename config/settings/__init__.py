import environ
import os

from django.contrib import messages

from pathlib import Path
from easy_thumbnails.conf import Settings as thumbnail_settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent
APP_DIR = BASE_DIR / "stories"
APPS_DIR = APP_DIR / "apps"

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env(
    "SECRET_KEY",
    default="AdakCqctVmwfe6I0EweI1iHsIq7VHaIZXTtGW5WGhtrMpwqfh6gleyIOOEjwZL7Y",
)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

TIME_ZONE = "America/New_York"
LANGUAGE_CODE = "en-US"
LOCALE_PATHS = [str(BASE_DIR / "locale")]

ALLOWED_HOSTS = []

# https://docs.djangoproject.com/en/dev/ref/settings/#languages
# from django.utils.translation import gettext_lazy as _
# LANGUAGES = [
#     ('en', _('English')),
#     ('fr-fr', _('French')),
#     ('pt-br', _('Portuguese')),
# ]

SITE_ID = 1
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# APPS

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
]

THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.mfa",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_spectacular",
    "webpack_loader",
    'easy_thumbnails',
    'image_cropping',
]

LOCAL_APPS = [
    "stories.apps.users",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# THUMBNAILS
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

# AUTHENTICATION
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "users:redirect"
LOGIN_URL = "account_login"

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

# URLS

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# TEMPLATES

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APP_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "stories.apps.users.context_processors.allauth_settings",
            ],
        },
    },
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default="postgres:///stories",
    ),
}
# STATIC

STATIC_URL = 'static/'

STATIC_ROOT = str(BASE_DIR / 'staticfiles')

STATICFILES_DIRS = [
    str(APP_DIR / "static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA

MEDIA_URL = '/media/'
MEDIA_ROOT = str(APP_DIR / 'media')

# FORMS

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"


# EMAIL

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)

EMAIL_TIMEOUT = 5
ACCOUNT_EMAIL_VERIFICATION = "none"

# ADMIN

ADMIN_URL = "admin/"
DJANGO_ADMIN_FORCE_ALLAUTH = env.bool("DJANGO_ADMIN_FORCE_ALLAUTH", default=False)

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}


# ALLAUTH

ACCOUNT_ALLOW_REGISTRATION = env.bool("ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_ADAPTER = "stories.apps.users.adapters.AccountAdapter"
ACCOUNT_FORMS = {"signup": "stories.apps.users.forms.UserSignupForm"}
SOCIALACCOUNT_ADAPTER = "stories.apps.users.adapters.SocialAccountAdapter"
SOCIALACCOUNT_FORMS = {"signup": "stories.apps.users.forms.UserSocialSignupForm"}

# DRF
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# CORS

CORS_URLS_REGEX = r"^/api/.*$"

# SPECTACULAR

SPECTACULAR_SETTINGS = {
    "TITLE": "Swayambhu Stories API",
    "DESCRIPTION": "Documentation of API endpoints of Swayambhu Stories",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SCHEMA_PATH_PREFIX": "/api/",
}

# WEBPACK

WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "STATS_FILE": BASE_DIR / "webpack-stats.json",
        "POLL_INTERVAL": 0.1,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    },
}
if DEBUG:
    THIRD_PARTY_APPS += [
        "debug_toolbar",
        "whitenoise.runserver_nostatic",
    ]
    
    DEBUG_TOOLBAR_CONFIG = {
        "DISABLE_PANELS": [
            "debug_toolbar.panels.redirects.RedirectsPanel",
            # Disable profiling panel due to an issue with Python 3.12:
            # https://github.com/jazzband/django-debug-toolbar/issues/1875
            "debug_toolbar.panels.profiling.ProfilingPanel",
        ],
        "SHOW_TEMPLATE_CONTEXT": True,
    }

if DEBUG:
    INSTALLED_APPS = [
        "debug_toolbar",
        "whitenoise.runserver_nostatic",
        "django_extensions",
        *INSTALLED_APPS,
    ]

    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    
    DEBUG_TOOLBAR_CONFIG = {
        "DISABLE_PANELS": [
            "debug_toolbar.panels.redirects.RedirectsPanel",
            # Disable profiling panel due to an issue with Python 3.12:
            # https://github.com/jazzband/django-debug-toolbar/issues/1875
            "debug_toolbar.panels.profiling.ProfilingPanel",
        ],
        "SHOW_TEMPLATE_CONTEXT": True,
    }

    WEBPACK_LOADER["DEFAULT"]["CACHE"] = not DEBUG

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }