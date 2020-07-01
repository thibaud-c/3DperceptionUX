from flask import request, json, Response, Blueprint, g
from ..models.UserModel import UserModel, UserSchema

user_api = Blueprint('user_api', __name__)
user_schema = UserSchema()

### create user + config

@user_api.route('/<user_id>', methods=['POST'])
def create(user_id):
  """
  Create User Function
  """
  req_data = request.get_json()
  isuser = UserModel.get_one_user(user_id)
  #Check if user exist
  if isuser:
    return custom_response({'error': 'User already exist'}, 400)

  req_data["user_guid"] = user_id

  user = UserModel(req_data)
  message = user.create_user()

  return custom_response({"message" :message}, 201)


### Put data in user

@user_api.route('/<user_id>', methods=['PUT'])
def update(user_id):
  """
  Update me
  """
  req_data = request.get_json()
  
  user = UserModel.get_one_user(user_id)
  #Check if user exist
  if not user:
    return custom_response({'error': 'user not found'}, 404)

  message = user.update(req_data)
  if not message:
    return custom_response({'error': 'data not saved'}, 404)
  #ser_user = user_schema.dump(user).data
  return custom_response({"message" :message}, 200)  


# DELETE ?

### Get User config 

@user_api.route('/config/<int:user_id>', methods=['GET'])
def get_userconfig(user_id):
  """
  Get a user config to order tasks
  """
  user_config = UserModel.get_user_config(user_id)
  if not user_config:
    return custom_response({'error': 'config not found'}, 404)
  
  return custom_response(user_config, 200)



### Delete user
@user_api.route('/<int:user_id>', methods=['DELETE'])
def delete(user_id):
  """
  Delete a user
  """
  user = UserModel.get_one_user(user_id)
  if not user:
    return custom_response({'error': 'user not found'}, 404)

  message = user.delete()
  
  return custom_response({'message': message}, 204)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )