import os

SECRET_KEY = 'projsoft'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'casa152251',
        servidor = 'eemv.c1luz7vbpipi.us-east-1.rds.amazonaws.com',
        database = 'projsoft'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'