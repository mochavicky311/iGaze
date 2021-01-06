import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    UPLOAD_FOLDER = 'scp300/static/recm/save/'
    SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1:3306/p300'
    SQLALCHEMY_TRACK_MODIFICATIONS = False