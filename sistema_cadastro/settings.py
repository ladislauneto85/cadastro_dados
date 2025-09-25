import os
from pathlib import Path
import dj_database_url
from decouple import config, Csv
from urllib.parse import quote_plus

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Use python-decouple para ler as variáveis de ambiente
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

# --- INÍCIO DA CORREÇÃO: ALLOWED_HOSTS (Versão Final e Robusta) ---
# Esta versão agora adiciona a URL de Deploy E a URL de Produção

hosts = ['127.0.0.1', 'localhost']

# Adiciona a URL de deploy (ex: dados-git-main...vercel.app)
VERCEL_DEPLOY_URL = os.environ.get('VERCEL_URL')
if VERCEL_DEPLOY_URL:
    hosts.append(VERCEL_DEPLOY_URL.replace('https://', ''))

# Adiciona a URL de Produção (ex: dados-omega.vercel.app)
VERCEL_PROD_URL = os.environ.get('VERCEL_PROJECT_PRODUCTION_URL')
if VERCEL_PROD_URL:
    hosts.append(VERCEL_PROD_URL.replace('https://', ''))

# Lê a variável de ambiente ALLOWED_HOSTS (para domínios customizados)
# Se não estiver definida, usa a lista de hosts que acabamos de criar.
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default=','.join(hosts),
    cast=Csv()
)
# --- FIM DA CORREÇÃO ---


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    # Minhas Apps
    'core',
    'pessoal',
    'funcional',
    'familiar',
    # Apps de Terceiros
    'crispy_forms',
    'crispy_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sistema_cadastro.urls'

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

WSGI_APPLICATION = 'sistema_cadastro.wsgi.application'


# Database
# Monta a URL do banco de dados programaticamente para lidar com senhas
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = quote_plus(config('DB_PASSWORD')) # Codifica a senha
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')

DATABASE_URL = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# --- INÍCIO DA CORREÇÃO 2: DATABASE SSL ---
# (Esta parte já estava correta, é para conectar ao Supabase)
DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL, 
        conn_max_age=600,
        ssl_require=True  # <-- Correção para Supabase
    )
}
# --- FIM DA CORREÇÃO 2 ---


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Bahia'
USE_I18N = True
USE_TZ = True


# Static and Media files
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # O WhiteNoise usará esta pasta
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Crispy Forms settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


# Login settings
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'