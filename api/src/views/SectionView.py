#/src/views/SectionView.py
from flask import request, g, Blueprint, json, Response
from ..models.SectionModel import SectionModel, SectionSchema

section_api = Blueprint('section_api', __name__)
section_schema = SectionSchema()


@section_api.route('/', methods=['POST'])
def create():
  """
  Create section Function
  """
  req_data = request.get_json()
  data = section_schema.load(req_data)
  post = SectionModel(data)
  post.save()
  data = section_schema.dump(post)
  return custom_response(data, 201)

@section_api.route('/', methods=['GET'])
def get_all():
  """
  Get All sections
  """
  posts = SectionModel.get_all_sections()
  data = section_schema.dump(posts, many=True)
  return custom_response(data, 200)


@section_api.route('/<int:section_id>', methods=['PUT'])
def update(section_id):
  """
  Update A section
  """
  req_data = request.get_json()
  post = SectionModel.get_one_section(section_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = section_schema.dump(post)
  if data.get('owner_id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  data= section_schema.load(req_data, partial=True)
  post.update(data)

  data = section_schema.dump(post)
  return custom_response(data, 200)

@section_api.route('/<int:section_id>', methods=['DELETE'])
def delete(section_id):
  """
  Delete A section
  """
  post = SectionModel.get_one_section(section_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = section_schema.dump(post)

  post.delete()
  return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )