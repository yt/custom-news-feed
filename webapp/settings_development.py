import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql', 
    'NAME': 'news_feed_db',
    'USER': os.environ["LOCAL_DB_USER"],
    'PASSWORD': os.environ["LOCAL_DB_PASSWORD"],
    'HOST': 'database',
    'PORT': '3306',
  }
}

