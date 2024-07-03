from database.db import get_connection
import psycopg2
import json

class Drink():
  def __init__(self, id, name, instructions, glass, image, alcohol, category, ingredients, measurements):
    self.id = id
    self.name = name
    self.instructions = instructions
    self.glass = glass
    self.image = image
    self.alcohol = alcohol
    self.category = category
    self.ingredients = ingredients
    self.measurements = measurements
    
  @classmethod
  def get_drinks(self):
    try:
      connection = get_connection()
      
      query = """
      SELECT id, name, instructions, glass, image, alcohol, category, ingredients, measurements 
      FROM drink 
      ORDER BY name ASC
      """
      
      drinks = []
      
      with connection.cursor() as cursor:
        cursor.execute(query)
        resultset = cursor.fetchall()
        
        for row in resultset:
          drink = Drink(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
          drink = drink.to_JSON()

          drinks.append(drink)
          
      connection.close()
      return drinks
    except Exception as ex:
      raise Exception(f"Error al obtener bebidas: {ex}")
    
  @classmethod
  def get_drink(self, id):
    try:
      connection = get_connection()
      
      query = """ 
      SELECT id, name, instructions, glass, image, alcohol, category, ingredients, measurements
      FROM drink
      WHERE id = %s
      """
      
      with connection.cursor() as cursor:
        cursor.execute(query,(id,))
        result = cursor.fetchone()
        
        drink = None
        
        if result != None:
          drink = Drink(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])
          drink = drink.to_JSON()
        
      connection.close()
      return drink
    
    except Exception as ex:
      raise Exception(f"Error al obtener la bebida: {ex}")
    
  @classmethod
  def add_drink(self, drink):
    try:
      connection = get_connection()
      
      query = """INSERT INTO drink (id, name, instructions, glass, image, alcohol, category, ingredients, measurements)
      VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
      """
      
      with connection.cursor() as cursor:
        cursor.execute(query, (drink.id, drink.name, drink.instructions, drink.glass, drink.image, drink.alcohol, drink.category, drink.ingredients, drink.measurements))
        
        affected_rows = cursor.rowcount
        connection.commit()
        
      connection.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)
    
  @classmethod
  def update_drink(self, drink):
    try:
      connection = get_connection()
      query = """
      UPDATE drink SET name = %s, instructions = %s, glass = %s, image = %s,
      alcohol = %s, category = %s, ingredients = %s, measurements = %s
      WHERE id = %s
      """
      
      with connection.cursor() as cursor:
        cursor.execute(query, (drink.name, drink.instructions, drink.glass, drink.image, drink.alcohol, drink.category, drink.ingredients, drink.measurements, drink.id))
        
        affected_rows = cursor.rowcount
        connection.commit()
        
      connection.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)  
  
  @classmethod
  def delete_drink(self, drink_id):
    try:
      connection = get_connection()
      
      with connection.cursor() as cursor:
        cursor.execute("DELETE FROM drink WHERE id = %s",(drink_id,))
        affected_rows = cursor.rowcount
        connection.commit()
        
      connection.close()
      return affected_rows
    except Exception as ex:
      raise Exception(ex)
    
  def to_JSON(self):
    return {
    'id': self.id,
    'name': self.name,
    'instructions': self.instructions,
    'glass': self.glass,
    'image': self.image,
    'alcohol': self.alcohol,
    'category': self.category,
    'ingredients':self.ingredients,
    'measurements':self.measurements
    }