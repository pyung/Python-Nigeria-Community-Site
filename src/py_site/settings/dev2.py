from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "7#lg*n6sm!&^9#g6xa-=q&+ht&&f3bjtj6j*ze+rfuz5+vi#ag"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = ["localhost", "127.0.0.1"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# INSTALLED_APPS += ["debug_toolbar","django_extensions"]
# MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

try:
    from .local import *
except ImportError:
    pass
