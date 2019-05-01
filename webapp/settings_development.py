import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql', 
    'NAME': os.getenv("LOCAL_DB_NAME", 'news_feed_db'),
    'USER': os.getenv("LOCAL_DB_USER"),
    'PASSWORD': os.getenv("LOCAL_DB_PASSWORD"),
    'HOST': os.getenv("LOCAL_DB_HOST", 'database'),
    'PORT': os.getenv("LOCAL_DB_PORT", 3306),
  }
}

