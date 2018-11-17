import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:1204@localhost/pitched_perfect'
      
class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True
 
config_options = {
'development':DevConfig,
'production':ProdConfig
} 

     