from flask import Blueprint, jsonify, request
from models.DrinkModel import Drink
from utils.create_drinks import create_drink
import uuid

main = Blueprint('drinks', __name__)

@main.route('/', methods=['GET'])
def get_all_drinks():
  try:
    drinks = Drink.get_drinks()
    return jsonify(drinks), 200
  except Exception as ex:
    return jsonify({'message': str(ex)}), 500

@main.route('/<drink_id>', methods=['GET'])
def get_drink(drink_id):
  try:
    drink = Drink.get_drink(drink_id)
    return jsonify(drink)
  except Exception as ex:
    return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_drink():
  try:
    data = request.get_json()
    
    drink = create_drink(data)
    
    affected_rows = Drink.add_drink(drink)
    
    if affected_rows == 1:
      return jsonify({'message': 'Trago creado con exito!'}), 201
    else:
      return jsonify({'message': 'Error al crear el nuevo trago'})
    
  except Exception as ex:
    raise Exception(ex)
  
@main.route('/update/<drink_id>', methods=['PUT'])
def update_drink(drink_id):
  try:
    data = request.get_json()
    drink = create_drink(data)

    affected_rows = Drink.update_drink(drink)
    
    if affected_rows == 1:
      return jsonify({'message': 'Trago actualizado con exito!'}), 204
    else:
      return jsonify({'message': 'No se pudo actualizar el trago'}), 404
  except Exception as ex:
    Exception(ex)

@main.route('/delete/<drink_id>', methods=['DELETE'])
def delete_drink(drink_id):
  try:
    affected_rows = Drink.delete_drink(drink_id)
    
    if affected_rows == 1:
      return jsonify({'message': 'Trago eliminado con exito!'}), 204
    else:
      return jsonify({'message': 'No se pudo eliminar el trago'}), 404
  except Exception as ex:
    raise Exception(ex)