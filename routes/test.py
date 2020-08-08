from flask import Blueprint, request, jsonify, Response
from database.models import Test
from file_manager import upload_images

test_router = Blueprint('test_router', __name__)


@test_router.route('/test', methods=['POST'])
def createTest():
  image = request.json['image']
  
  url = upload_images.upload(image)

  body = request.get_json()
  body['image'] = url

  result = Test(**body).save()
  id = result.id
  return {'id': str(id)}, 201
  

@test_router.route('/test', methods=['GET'])
def listTests():
  tests = Test.objects().to_json()
  return Response(tests, mimetype="application/json", status=200)
