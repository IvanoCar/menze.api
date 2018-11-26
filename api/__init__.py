from flask import Flask
from flask_pymongo import PyMongo
from api.modules.utils.auth import Auth
from api.modules.utils.utility import Utils

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'NAME'
app.config['MONGO_URI'] = 'URI'

app.secret_key = 'SECRET'

mongo = PyMongo(app)
authenticate = Auth()

status = {
    'STATUS': 0,
    'VERSION': '1.0'
}

from api.modules.update.routes import update
from api.modules.get.routes import get
from api.modules.show.routes import show
from api.modules.dataport.routes import port

app.register_blueprint(update)
app.register_blueprint(get)
app.register_blueprint(show)
app.register_blueprint(port)


if __name__ == '__main__':
    app.run()
