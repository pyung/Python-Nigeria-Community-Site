from .base import *
import environ

env = environ.Env()
DEBUG = True

ALLOWED_HOSTS = ['arcane-ocean-27558.herokuapp.com']
try:
    from .local import *
except ImportError:
    pass


DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    "default": env.db("DATABASE_URL"),
    # read os.environ['SQLITE_URL']
}


MIDDLEWARE = ["whitenoise.middleware.WhiteNoiseMiddleware"] + MIDDLEWARE

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

SECRET_KEY=env('SECRET_KEY')