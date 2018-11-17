from app import create_app,db
from app.models import User
from flask_script import Manager,Server
# from app.models import User


app = create_app('production')
manager = Manager(app)
manager.add_command('server',Server)

if __name__ == '__main__':
   manager.run()