import os
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('powerfulsecretkey')
    WTF_CSRF_SECRET_KEY="a csrf secret key"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mango:mango@localhost/pitch'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}