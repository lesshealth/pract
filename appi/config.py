import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'regist.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '8Rgr5g75rBRru5urFH%BJ57b'