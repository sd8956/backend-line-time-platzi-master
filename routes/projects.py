from flask import Blueprint, request, jsonify, Response
from database.models import home_project
from file_manager import upload_images

projects_router = Blueprint('projects_router', __name__)

@projects_router.route('/projects', methods=['POST'])
def createProject():
  #image = request.json['image']
  
  #url = upload_images.upload(image)

  new_project = request.get_json()
  #new_project['image'] = url
  
  result = home_project(**new_project).save()
  id = result.id
  return {'id': str(id)}, 201

@projects_router.route('/projects', methods=['GET'])
def listProjects():
  projects = home_project.objects().to_json()
  return Response(projects, mimetype="application/json", status=200)
