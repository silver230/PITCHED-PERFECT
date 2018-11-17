import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:1204@localhost/my_pitch'
      
class ProdConfig(Config):
 
 
class DevConfig(Config):
    DEBUG = True
 
config_options = {
'development':DevConfig,
'production':ProdConfig
} 

     