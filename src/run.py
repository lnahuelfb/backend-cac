from flask import Flask , jsonify, request
from config import config
from routes import Drink

app = Flask(__name__)

if __name__ == '__main__':
  app.config.from_object(config['development'])
  
  #Blueprints
  app.register_blueprint(Drink.main, url_prefix='/api/drinks')
  
  app.run()