from marshmallow import fields, Schema
import datetime
from . import db
from sqlalchemy import JSON
from cfg import *

class UserModel(db.Model):
  """
  User Model
  """

  # table name
  __tablename__ = TABLENAME
  # init
  user_guid = db.Column(db.String(36), unique=True, primary_key=True)
  start_at = db.Column(db.DateTime)
  end_at = db.Column(db.DateTime)
  language = db.Column(db.Integer)
  version = db.Column(db.Integer)
  scenes_order = db.Column(db.ARRAY(db.Integer))
  answers_order = db.Column(db.ARRAY(db.Integer))
  angles_order = db.Column(db.ARRAY(db.Float))
  user_tech_config = db.Column(JSON)
  # SOCIO
  age = db.Column(db.Integer, nullable=False)
  gender = db.Column(db.Integer, nullable=False)
  education = db.Column(db.Integer, nullable=False)
  grew_density = db.Column(db.Integer)
  grew_country = db.Column(db.String(128))
  location_density = db.Column(db.Integer)
  location_country = db.Column(db.String(128))
  frequency_3d = db.Column(db.Integer, nullable=False)
  exercice_spatial = db.Column(db.Integer, nullable=False)
  # Question
  tuto_time = db.Column(db.Integer, nullable=False)
  E0Q0 = db.Column(JSON, nullable=False)
  E0Q1 = db.Column(JSON, nullable=False)
  E0Q2 = db.Column(JSON, nullable=False)
  E1Q0 = db.Column(JSON, nullable=False)
  E1Q1 = db.Column(JSON, nullable=False)
  E1Q2 = db.Column(JSON, nullable=False)
  E2Q0 = db.Column(JSON, nullable=False)
  E2Q1 = db.Column(JSON, nullable=False)
  E2Q2 = db.Column(JSON, nullable=False)
  E2Q3 = db.Column(JSON, nullable=False)
  E3Q0 = db.Column(JSON, nullable=False)
  E3Q1 = db.Column(JSON, nullable=False)
  E3Q2 = db.Column(JSON, nullable=False)
  E3Q3 = db.Column(JSON, nullable=False)
  # Feedback
  pref_hard = db.Column(db.Integer, nullable=False)
  pref_easy = db.Column(db.Integer, nullable=False)
  pref_memory = db.Column(db.Integer, nullable=False)
  pref_static = db.Column(db.Integer, nullable=False)
  estim_building = db.Column(db.Integer, nullable=False)
  smile = db.Column(db.Integer, nullable=False)
  difficulty = db.Column(db.Integer, nullable=False)
  comment = db.Column(db.String(1024), nullable=False)
  followup = db.Column(db.Integer, nullable=False)
  email = db.Column(db.String(256), nullable=False)
  score = db.Column(db.Integer, nullable=False)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    # INIT
    self.user_guid = data.get('user_guid')
    self.start_at = data.get('start_at')
    self.end_at = data.get('end_at')
    self.language = data.get('language')
    self.version = data.get('version')
    self.scenes_order = data.get('scenes_order')
    self.answers_order = data.get('answers_order')
    self.angles_order = data.get('angles_order')
    self.user_tech_config = data.get('user_tech_config')
    # SOCIO
    self.age = data.get('age')
    self.gender = data.get('gender')
    self.education = data.get('education')
    self.grew_density = data.get('grew_density')
    self.grew_country = data.get('grew_country')
    self.location_density = data.get('location_density')
    self.location_country = data.get('location_country')
    self.frequency_3d = data.get('frequency_3d')
    self.exercice_spatial = data.get('exercice_spatial')
    # Question
    self.tuto_time = data.get('tuto_time')
    self.E0Q0 = data.get('E0Q0')
    self.E0Q1 = data.get('E0Q1')
    self.E0Q2 = data.get('E0Q2')
    self.E1Q0 = data.get('E1Q0')
    self.E1Q1 = data.get('E1Q1')
    self.E1Q2 = data.get('E1Q2')
    self.E2Q0 = data.get('E2Q0')
    self.E2Q1 = data.get('E2Q1')
    self.E2Q2 = data.get('E2Q2')
    self.E2Q3 = data.get('E2Q3')
    self.E3Q0 = data.get('E3Q0')
    self.E3Q1 = data.get('E3Q1')
    self.E3Q2 = data.get('E3Q2')
    self.E3Q3 = data.get('E3Q3')
    # Feedback
    self.pref_hard = data.get('pref_hard')
    self.pref_easy = data.get('pref_easy')
    self.pref_memory = data.get('pref_memory')
    self.pref_static = data.get('pref_static')
    self.estim_building = data.get('estim_building')
    self.smile = data.get('smile')
    self.difficulty = data.get('difficulty')
    self.comment = data.get('comment')
    self.followup = data.get('followup')
    self.email = data.get('email')
    self.score = data.get('score')

  def create_user(self):
    db.session.add(self)
    db.session.commit()
    return "User created"

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    db.session.commit()
    return "saved"

  def delete(self):
    db.session.delete(self)
    db.session.commit()
    return "deleted"

  @staticmethod
  def get_one_user(id):
    return UserModel.query.get(id)

  @staticmethod
  def get_all_user():
    return UserModel.query.filter(UserModel.score != None).all()
  
  def __repr(self):
    return '<id {}>'.format(self.id)

class UserSchema(Schema):
  # INIT
  user_guid = fields.Str(required=False)
  start_at = fields.DateTime(required=False)
  end_at = fields.DateTime(required=False)
  language = fields.Int(required=False)
  version = fields.Int(required=False)
  scenes_order = fields.List(fields.Int(required=False))
  answers_order = fields.List(fields.Float(required=False))
  angles_order = fields.List(fields.Int(required=False))
  user_tech_config = fields.Dict(required=False)
  # SOCIO
  age = fields.Int(required=False)
  gender = fields.Int(required=False)
  education = fields.Int(required=False)
  grew_density = fields.Int(required=False)
  grew_country = fields.Str(required=False)
  location_density = fields.Int(required=False)
  location_country = fields.Str(required=False)
  frequency_3d = fields.Int(required=False)
  exercice_spatial = fields.Int(required=False)
  # Question
  tuto_time = fields.Int(required=False)
  E0Q0 = fields.Dict(required=False)
  E0Q1 = fields.Dict(required=False)
  E0Q2 = fields.Dict(required=False)
  E1Q0 = fields.Dict(required=False)
  E1Q1 = fields.Dict(required=False)
  E1Q2 = fields.Dict(required=False)
  E2Q0 = fields.Dict(required=False)
  E2Q1 = fields.Dict(required=False)
  E2Q2 = fields.Dict(required=False)
  E2Q3 = fields.Dict(required=False)
  E3Q0 = fields.Dict(required=False)
  E3Q1 = fields.Dict(required=False)
  E3Q2 = fields.Dict(required=False)
  E3Q3 = fields.Dict(required=False)
  #Feedback
  pref_hard = fields.Int(required=False)
  pref_easy = fields.Int(required=False)
  pref_memory = fields.Int(required=False)
  pref_static = fields.Int(required=False)
  estim_building = fields.Int(required=False)
  smile = fields.Int(required=False)
  difficulty = fields.Int(required=False)
  comment = fields.Str(required=False)
  followup = fields.Int(required=False)
  email = fields.Str(required=False)
  score = fields.Int(required=False)