import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'ABigSecretIsHardToFind'
DATABASE_CONNECTION_OPTIONS = {}
DEBUG = True
HOST = '0.0.0.0'
PORT = 8080
SECRET_KEY = 'AnotherBigSecretIsAlsoHardToFind'
SECURITY_PASSWORD_HASH = 'sha256_crypt'
SECURITY_PASSWORD_SALT = 'ThisIsNotALoveSong'
SECURITY_REGISTERABLE=False
SECURITY_REGISTER_EMAIL=False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data/local.db')
THREADS_PER_PAGE = 8
VOUCHER_MAXAGE = 120
