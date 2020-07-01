from flask import Flask
from flask_cors import CORS

import logging

from .config import app_config
from .models import db

# import user_api blueprint
from .views.UserView import user_api as user_blueprint

def create_app(env_name):
  """
  Create app
  """
  #init log
  logging.basicConfig(filename='Flask.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

  # app initiliazation
  app = Flask(__name__)
  CORS(app)
  app.config.from_object(app_config[env_name])

  # initializing db
  db.init_app(app)

  app.register_blueprint(user_blueprint, url_prefix='/api/v1/')

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Server is running...'

  return app