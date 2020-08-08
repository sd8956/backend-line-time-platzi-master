from flask import Flask
from database.db import initialize_db
from flask_cors import CORS
from routes import courses, projects, sessions, test
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
 
app.config['MONGODB_SETTINGS'] = {
    'host': f'mongodb+srv://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DB_NAME")}?retryWrites=true&w=majority'
}

initialize_db(app)

CORS(app)

app.register_blueprint(courses.courses_router)
app.register_blueprint(projects.projects_router)
app.register_blueprint(sessions.sessions_router)
app.register_blueprint(test.test_router)

if __name__ == '__main__':
  port = os.getenv('PORT')
  debug = os.getenv('DEBUG') == 'True'

  app.run(port=port, debug=debug)
