from .db import db

class Test(db.Document):
  test = db.StringField(required=True)
  image = db.StringField(required=True)

class Session(db.Document):
  title = db.StringField(required=True)
  description = db.StringField(required=True)

class Project(db.Document):
  title = db.StringField(required=True)
  description = db.StringField(required=True)
  image = db.StringField(required=True)
  url = db.StringField(required=True)
  tec = db.StringField(required=True)

class Course(db.Document):
  title = db.StringField(required=True)
  image = db.StringField(required=True)