import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql', 
    'NAME': os.getenv("DB_NAME", 'news_feed_db'),
    'USER': os.getenv("DB_USER"),
    'PASSWORD': os.getenv("DB_PASSWORD"),
    'HOST': os.getenv("DB_HOST", 'database'),
    'PORT': os.getenv("DB_PORT", 3306),
  }
}

