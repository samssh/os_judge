import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-p3s+(_krg$9fk-waxcany^b(fw$l2rt&w-d7&9@5qv^xbckhh1'

DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'account',
    'judge',
    "django_celery_results",
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

ROOT_URLCONF = 'os_judge.urls'

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

WSGI_APPLICATION = 'os_judge.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": os.getenv('DB_NAME', "os_judge_db"),
        "USER": os.getenv('DB_USER', "os_judge_user"),
        "PASSWORD": os.getenv('DB_PASS', "os_judge_password"),
        "HOST": os.getenv('DB_HOST', "localhost"),
        "PORT": os.getenv('DB_PORT', 5432),
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = './static_root'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
LOGIN_URL = '/users/login/'
LOGOUT_REDIRECT_URL = '/users/login'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

RABBITMQ_CELERY_URL = "amqp://{user_name}:{password}@{host}:{port}/{vhost}".format(
    host=os.getenv('RABBITMQ_HOST', 'localhost'),
    port=os.getenv('RABBITMQ_PORT', '5672'),
    user_name=os.getenv('RABBITMQ_USER', 'test_user'),
    password=os.getenv('RABBITMQ_PASSWORD', 'test_password'),
    vhost=os.getenv('RABBITMQ_VHOST', '')
)
# Celery
CELERY_BROKER_URL = RABBITMQ_CELERY_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_BACKEND_ALWAYS_RETRY = True
CELERY_RESULT_BACKEND = 'django-db'

task_annotations = {'*': {'rate_limit': '5/m'}}

TEST_COUNT = 8
