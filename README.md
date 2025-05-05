sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update

sudo apt install python3.11-full

pip install Django

pip install djangorestframework

pip install django-filter

pip install psycopg2

pip install drf-spectacular

python manage.py makemigrations

python manage.py migrate

django-admin startproject tutorial .

python manage.py createsuperuser

python manage.py runserver

django-admin startapp quickstart

pip install coverage 

overage run --source='.' manage.py test .

pip install ruff

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'quickstart.apps.QuickstartConfig',
]
REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'main_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '6432',
    }
}
```

https://www.django-rest-framework.org/topics/documenting-your-api/

https://www.transfernow.net/dl/20250505OJpvvboL