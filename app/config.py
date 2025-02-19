import os

class Config(object):
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload/'
    SERVER_PATH = ROOT + UPLOAD_PATH

    USER = os.environ.get('POSTGRES_USER', 'aladinskiy')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'qwertyuio')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', 5532)
    DB = os.environ.get('POSTGRES_DB', 'mydb')
    SQLALCHEMY_DATABASE_URI = F'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = 'qwertyuioasdfghjkl'
    SQLALCHEMY_TRACK_MODIFICATIONS = True