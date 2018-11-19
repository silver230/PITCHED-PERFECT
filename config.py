import os

class Config:
    SECRET_KEY = '120dsaf4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:1204@localhost/pitched_perfect'
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'sylveromondipitched_perfect'
    SENDER_EMAIL = 'sylveromondi@gmail.com'
    
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringashool:1204@localhost/my_pitch_test'
class DevConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:1204@localhost/pitched_perfect'

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}    