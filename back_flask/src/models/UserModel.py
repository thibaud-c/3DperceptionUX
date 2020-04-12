from marshmallow import fields, Schema
import datetime
from . import db
from sqlalchemy.dialects.postgresql import JSON

class UserModel(db.Model):
  """
  User Model
  """

  # table name
  __tablename__ = 'perception_ux'
  #config
  id_poste = db.Column(db.Integer, unique=True, primary_key=True)
  config = db.Column(JSON, nullable=False)
  #Socio
  age = db.Column(db.Integer, nullable=False)
  genre = db.Column(db.Integer, nullable=False)
  education = db.Column(db.Integer, nullable=False)
  education_other = db.Column(db.String(128))
  location = db.Column(db.Integer, nullable=False)
  location_zipcode = db.Column(db.Integer)
  location_density = db.Column(db.Integer)
  grew = db.Column(db.Integer, nullable=False)
  grew_zipcode = db.Column(db.Integer)
  grew_density = db.Column(db.Integer)
  grew_country = db.Column(db.String(128))
  frequency_3d = db.Column(db.Integer, nullable=False)
  technology_3d = db.Column(db.ARRAY(db.Integer))
  technology_3d_other = db.Column(db.String(128))
  participation = db.Column(db.Integer, nullable=False)
  participation_3d = db.Column(db.Integer)
  participation_role = db.Column(db.ARRAY(db.Integer))
  participation_role_other = db.Column(db.String(128))
  participation_sujet = db.Column(db.Integer)
  participation_sujet_other = db.Column(db.String(128))
  participation_number = db.Column(db.Integer)
  colorblind_rg = db.Column(db.Integer, nullable=False)
  colorblind_dc = db.Column(db.Integer, nullable=False)
  colorblind_pt = db.Column(db.Integer, nullable=False)
  exercice_3d = db.Column(db.Integer, nullable=False)
  #LOD
  E0Q0 = db.Column(db.Integer, nullable=False)
  E0Q1 = db.Column(db.Integer, nullable=False)
  E0Q2 = db.Column(db.Integer, nullable=False)
  E1Q0 = db.Column(db.Integer, nullable=False)
  E1Q1 = db.Column(db.Integer, nullable=False)
  E1Q2 = db.Column(db.Integer, nullable=False)
  E1Q3 = db.Column(db.Integer, nullable=False)
  E1Q4 = db.Column(db.Integer, nullable=False)
  E0Time = db.Column(db.Integer, nullable=False)
  E1Time = db.Column(db.Integer, nullable=False)
  #Feedback
  smile = db.Column(db.Integer, nullable=False)
  difficulty = db.Column(db.Integer, nullable=False)
  opinion3dpart = db.Column(db.Integer, nullable=False)
  comment = db.Column(db.String(1024), nullable=False)
  followup = db.Column(db.Integer, nullable=False)
  email = db.Column(db.String(256), nullable=False)
  #modified_at = db.Column(db.DateTime)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    #config
    self.id_poste = data.get('poste')
    self.config = data.get('config')
    #Socio
    self.age = data.get('age')
    self.genre = data.get('genre')
    self.education = data.get('education')
    self.education_other = data.get('education_other')
    self.location = data.get('location')
    self.location_zipcode = data.get('location_zipcode')
    self.location_density = data.get('location_density')
    self.grew = data.get('grew')
    self.grew_zipcode = data.get('grew_zipcode')
    self.grew_density = data.get('grew_density')
    self.grew_country = data.get('grew_country')
    self.frequency_3d = data.get('frequency_3d')
    self.technology_3d = data.get('technology_3d')
    self.technology_3d_other = data.get('technology_3d_other')
    self.participation = data.get('participation')
    self.participation_3d = data.get('participation_3d')
    self.participation_role = data.get('participation_role')
    self.participation_role_other = data.get('participation_role_other')
    self.participation_sujet = data.get('participation_sujet')
    self.participation_sujet_other = data.get('participation_sujet_other')
    self.participation_number = data.get('participation_number')
    self.colorblind_rg = data.get('colorblind_rg')
    self.colorblind_dc = data.get('colorblind_dc')
    self.colorblind_pt = data.get('colorblind_pt')
    self.exercice_3d = data.get('exercice_3d')
    #LOD
    self.E0Q0 = data.get('E0Q0')
    self.E0Q1 = data.get('E0Q1')
    self.E0Q2 = data.get('E1Q2')
    self.E1Q0 = data.get('E0Q0')
    self.E1Q1 = data.get('E1Q1')
    self.E1Q2 = data.get('E1Q2')
    self.E1Q3 = data.get('E1Q3')
    self.E1Q4 = data.get('E1Q4')
    self.E0Time = data.get('E0Time')
    self.E1Time = data.get('E1Time')
    #Feedback
    self.smile = data.get('smile')
    self.difficulty = data.get('difficulty')
    self.opinion3dpart = data.get('opinion3dpart')
    self.comment = data.get('comment')
    self.followup = data.get('followup')
    self.email = data.get('email')
    #self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()
    return "User created"

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    #self.modified_at = datetime.datetime.utcnow()
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
  def get_user_config(id):
    return UserModel.query.filter_by(id_poste=id).first().config
  
  def __repr(self):
    return '<id {}>'.format(self.id)

class UserSchema(Schema):
  #Config
  id_poste = fields.Int(required=False)
  config = fields.Str(required=False)
  #Socio
  age = fields.Int(required=False)
  genre = fields.Int(required=False)
  education = fields.Int(required=False)
  education_other = fields.Str(required=False)
  location = fields.Int(required=False)
  location_zipcode = fields.Int(required=False)
  location_density = fields.Int(required=False)
  grew = fields.Int(required=False)
  grew_zipcode = fields.Int(required=False)
  grew_density = fields.Int(required=False)
  grew_country = fields.Str(required=False)
  frequency_3d = fields.Int(required=False)
  technology_3d = fields.List(fields.Int(required=False))
  technology_3d_other = fields.Str(required=False)
  participation = fields.Int(required=False)
  participation_3d = fields.Int(required=False)
  participation_role = fields.List(fields.Int(required=False))
  participation_role_other = fields.Str(required=False)
  participation_sujet = fields.Int(required=False)
  participation_sujet_other = fields.Str(required=False)
  participation_number = fields.Int(required=False)
  colorblind_rg = fields.Int(required=False)
  colorblind_dc = fields.Int(required=False)
  colorblind_pt = fields.Int(required=False)
  exercice_3d = fields.Int(required=False)
  #LOD
  E0Q0 = fields.Int(required=False)
  E0Q1 = fields.Int(required=False)
  E0Q2 = fields.Int(required=False)
  E1Q0 = fields.Int(required=False)
  E1Q1 = fields.Int(required=False)
  E1Q2 = fields.Int(required=False)
  E1Q3 = fields.Int(required=False)
  E1Q4 = fields.Int(required=False)
  E0Time = fields.Int(required=False)
  E1Time = fields.Int(required=False)
  #Feedback
  smile = fields.Int(required=False)
  difficulty = fields.Int(required=False)
  opinion3dpart = fields.Int(required=False)
  comment = fields.Str(required=False)
  followup = fields.Int(required=False)
  email = fields.Str(required=False)
  #modified_at = fields.DateTime(dump_only=True)
