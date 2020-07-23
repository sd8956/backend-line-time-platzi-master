from flask import Blueprint, request, jsonify, Response
from database.models import Course
from file_manager import upload_images

courses_router = Blueprint('courses_router', __name__)

@courses_router.route('/courses', methods=['POST'])
def createCourse():
  image = request.files['image']
  
  url = upload_images.upload(image)

  new_course = request.get_json()
  new_course['image'] = url

  result = Course(**new_course).save()
  id = result.id
  return {'id': str(id)}, 201

@courses_router.route('/courses', methods=['GET'])
def listCourses():
  courses = Course.objects().to_json()
  return Response(courses, mimetype="application/json", status=200)
