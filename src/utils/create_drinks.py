from models.DrinkModel import Drink
import uuid

def create_drink(data):
  name = data['name']
  instructions = data['instructions']
  glass = data['glass']
  image = data['image']
  alcohol = float(data['alcohol'])
  category = data['category']
  ingredients = data['ingredients']
  measurements = data['measurements']
  
  if 'id' not in data or not data['id']:
    print('Creado nuevo uuid')
    id = str(uuid.uuid4())
  
  else:
    print(data['id'])
    id = str(data['id'])
  
  drink = Drink(id, name, instructions, glass, image, alcohol, category, ingredients, measurements)
  
  return drink