from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify
from app.auth.model import User

auth = Blueprint('auth', __name__, template_folder='templates',
                 static_folder='static')


@auth.route('/')
def index():
  return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup():
  content = request.get_json()
  user = User(name=content.get('name'),
              passwd=content.get('passwd'),
              passwdRepeat=content.get('passwdRepeat'))

  return jsonify(content)


@auth.route('/login', methods=['POST'])
def login():

  return jsonify(request.json)
