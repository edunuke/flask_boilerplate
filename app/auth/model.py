from flask_mongoalchemy import MongoAlchemy
import datetime
db = MongoAlchemy()


class User(db.Document):
  name = db.StringField()
  passwd = db.StringField()
  passwdRepeat = db.StringField()
  createdAt = db.DateTimeField(default=datetime.datetime.now)
