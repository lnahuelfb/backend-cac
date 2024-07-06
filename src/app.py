from flask import Flask , jsonify, request
from config import config
from routes import Drink
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={'*'})

if __name__ == '__main__':
  app.config.from_object(config['development'])

  app.register_blueprint(Drink.main, url_prefix='/api/drinks')

  app.run()