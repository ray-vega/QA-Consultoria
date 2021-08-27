from pathlib import Path
# from .settings import *

MYSQL ={
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': '171118',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'postgres',
        'PASSWORD': '171118',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
