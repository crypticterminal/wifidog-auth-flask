import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

APP_VERSION = '0.6.0'
DATABASE_CONNECTION_OPTIONS = {}
DEBUG = True
HOST = '0.0.0.0'
INFLUXDB_DATABASE = 'auth'
PORT = 8080
PUSH_ENABLED = False
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_POST_LOGIN_VIEW = 'app.vouchers_index'
SECURITY_POST_LOGOUT_VIEW = 'login'
SECURITY_REGISTERABLE=False
SECURITY_REGISTER_EMAIL=False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data/local.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
THREADS_PER_PAGE = 8
UPLOADS_DEFAULT_DEST = os.path.join(BASE_DIR, 'uploads')
UPLOADS_DEFAULT_URL = '/static'
VOUCHER_DEFAULT_MINUTES = 90
VOUCHER_MAXAGE = 60 * 24
