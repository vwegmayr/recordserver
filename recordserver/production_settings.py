# Django settings for recordserver project.
import os

PROJDIR = os.path.dirname(__file__)
BASEDIR = os.path.dirname(PROJDIR)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [u"80.218.0.179",u"192.168.0.59",u"127.0.0.1"]

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '%s/smtserve.db' % BASEDIR,
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = "%s/media" % BASEDIR

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

STATICFILES_DIRS = (
    os.path.join(PROJDIR, "static"),
)
STATIC_URL = '/static/'
STATIC_ROOT = "%s/static" % BASEDIR

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
#SECRET_KEY = '9z=5q&2h)8lu0g9^&xr8u+72kdg=epsh!)-9bkqr)4%uygbzj0'
SECRET_KEY = os.environ['SECRET_KEY']

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'recordserver.urls'

TEMPLATE_DIRS = (
    "%s/templates" % BASEDIR,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'sumatra_server',
    'sumatra.web',
    'sumatra.recordstore.django_store',
    'tagging',
    'registration',
)

LOGIN_REDIRECT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window for registration

WSGI_APPLICATION = 'recordserver.wsgi.application'

#X_FRAME_OPTIONS = "DENY"
#CSRF_COOKIE_HTTPONLY = True
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
#SECURE_SSL_REDIRECT = True
#SECURE_BROWSER_XSS_FILTER = True
#SECURE_CONTENT_TYPE_NOSNIFF = True

try:
    from local_settings import *
except ImportError:
    pass

