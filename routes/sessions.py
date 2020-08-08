from flask import Blueprint, request, jsonify, Response
from database.models import home_session

sessions_router = Blueprint('sessions_router', __name__)

@sessions_router.route('/sessions', methods=['POST'])
def createSession():
  body = request.get_json()
  session = home_session(**body).save()
  id = session.id
  return {'id': str(id)}, 201


@sessions_router.route('/sessions', methods=['GET'])
def listSessions():
  sessions = home_session.objects().to_json()
  return Response(sessions, mimetype="application/json", status=200)
