from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://moringaschool:1204@localhost/test'
    app.config.from_object(config_options[config_name])
    
    
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # registering the main app blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app 