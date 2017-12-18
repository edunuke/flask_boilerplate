import flask_login
from flask import url_for
from flask import Flask
from app.main.controllers import main
from app.auth.controllers import auth
from app.auth.model import db


app = Flask(__name__,)
app.secret_key = '123456789'  # Change this!
app.config['MONGOALCHEMY_DATABASE'] = 'application'
db.init_app(app)



app.register_blueprint(main, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')
