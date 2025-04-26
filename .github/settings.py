from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!hx@8^s#k)7t$6&b2e%*g+mf3q9l1o4r5u6y7i8o9p0'  # تم تغيير المفتاح
DEBUG = True  # تم التغيير لعرض الأخطاء
ALLOWED_HOSTS = ['*']  # السماح بجميع الاتصالات

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fleet_app'  # تأكد من تطابق اسم التطبيق
    'rest_framework',  # إضافة لدعم الواجهات البرمجية
]

# إضافة إعدادات المصادقة
AUTH_USER_MODEL = 'fleet_app.Employee'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'ar-sa'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEBUG = True  # تم التغيير لعرض الأخطاء
ALLOWED_HOSTS = ['*']  # السماح بجميع الاتصالات