from flask import request, json, Response, Blueprint, g
from ..models.UserModel import UserModel, UserSchema
import time

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

### Get score 

@user_api.route('/<user_id>/scores', methods=['GET'])
def results(user_id):
  """
  Create User Function
  """
  users = UserModel.get_all_user()
  scores = []
  speeds = []
  user_score = None
  user_speed = None
  for user in users:
    if user.user_guid == user_id:
      if user.end_at is None :
        print("notfound -> relaunch")
        time.sleep(0.5)
        results(user_id)
      user_speed = user.end_at - user.start_at
      user_score = user.score
    scores.append(user.score)
    speeds.append(user.end_at - user.start_at)
  speeds = sorted(speeds)
  scores = sorted(scores)
  data = {"score" :user_score,"nb_user":len(users),"top_speed":(len(users)-speeds.index(user_speed))/len(users),"top_score":1-((len(users)-scores.index(user_score))/len(users))}
  return custom_response({"data" :data}, 201)

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