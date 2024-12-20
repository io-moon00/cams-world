
"""
Django settings for coachLamont project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
import json


with open('config.json') as config_file:
    config = json.load(config_file)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '82.165.79.181',
	'coachlamont.de',
    'cams-world.de',
    'coachcamlam.de',
    'coachlamont.com',
    '*'
]
# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django_recaptcha',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'forms',
    'django_ckeditor_5',
    'compressor',
    'adminsortable2',
]

customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': '#6EA0D2',
            'label': 'Blue'
        },
    ]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', ],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough', '|', 'sourceEditing',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', '|', 'outdent', 'indent', 
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1 color-red' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2 color-red' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3 color-red' },
                { 'model': 'heading4', 'view': 'h4', 'title': 'Heading 4', 'class': 'ck-heading_heading4 color-red' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'false',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

CKEDITOR_5_FILE_UPLOAD_PERMISSION = "staff" 
COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_URL = '/static/'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coachLamont.urls'

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
                'main.context_processors.athletes',
                'main.context_processors.social_media', 
            ],
        },
    },
]

WSGI_APPLICATION = 'coachLamont.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Email settings
DEFAULT_FROM_EMAIL = 'Cams World <info@cams-world.de>'  # Name unter dem die E-Mail verschickt wird und die dazugehörige E-Mail-Adresse
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #'django.core.mail.backends.smtp.EmailBackend'  # SMTP-Backend
EMAIL_HOST = 'smtp.strato.de'
EMAIL_PORT = 587 # oder 587 oder was immer der Port deines E-Mail-Providers ist
EMAIL_USE_TLS = True  # Verbindung benutzt TLS-Verschlüsselung
EMAIL_HOST_USER = config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')  
MEDIA_URL = '/media/'

STATIC_ROOT =  os.path.join(BASE_DIR, 'static')  
STATIC_URL = '/static/'

JAZZMIN_SETTINGS ={
"site_logo": "../media/public/camsworld_logo_notext.svg",
"site_title": "Admin - Cams World",
"copyright": "camsworld",
"welcome_sign": "Welcome to Cams World Admin",
"site_brand": "Cams World",
"icons":{
    "auth": "fas fa-users-cog",
    "auth.Group": "fas fa-users",
    "auth.user": "fas fa-user",
    "main.Image": "fas fa-image",
    "main.Athlete": "fas fa-users",
    "main.Page": "fas fa-file",
    "main.CareerStage": "fas fa-list",
    "main.AboutSection": "fas fa-address-card",
    "main.Post": "fas fa-clipboard",
    "main.ContactData": "fas fa-address-book",
    "main.AthleteImage": "fas fa-image",
    "main.MyImage": "fas fa-image",
    "main.PostTag": "fas fa-tag",
    "main.SocialMedia": "fas fa-hashtag",
},
"topmenu_links": [
    # Url that gets reversed (Permissions can be added)
    {"name": "Webseite",  "url":  "/"},

    # model admin to link to (Permissions checked against model)
    {"model": "auth.User"},

    # App with dropdown menu to all its models pages (Permissions checked against models)
    {"app": "main"},
],

"usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
"show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": ["auth"],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

"custom_css": "backend.css",

"order_with_respect_to": ["main", "main.Page", "main.Post", "main.Image", "main.Athlete", "main.AboutSection", "main.MyImage", "main.CareerStage", "main.PostTag", "main.ContactData", "auth"],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "cerulean",
}

# Recaptcha
RECAPTCHA_PUBLIC_KEY = '6LcfZIolAAAAANsnf9OHUNIJ0CQDiuFv16gLrs6r'
RECAPTCHA_PRIVATE_KEY = config['RECAPTCHA_PRIVATE_KEY']
RECAPTCHA_REQUIRED_SCORE = 0.85
