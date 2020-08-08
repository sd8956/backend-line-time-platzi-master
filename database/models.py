from .db import db

class Test(db.Document):
  test = db.StringField(required=True)
  image = db.StringField(required=True)

class home_session(db.Document):
  title = db.StringField(required=True)
  description = db.StringField(required=True)

class home_project(db.Document):
  title = db.StringField(required=True)
  description = db.StringField(required=True)
  image = db.StringField(required=True)
  url = db.StringField(required=True)
  tec = db.StringField(required=True)

class home_course(db.Document):
  title = db.StringField(required=True)
  image = db.StringField(required=True)