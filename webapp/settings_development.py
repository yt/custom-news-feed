import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql', 
    'NAME': 'mysql_db',
    'USER': os.getenv("LOCAL_DB_USER"),
    'PASSWORD': os.getenv("LOCAL_DB_PASSWORD"),
    'HOST': 'database',
    'PORT': '3306',
  }
}

