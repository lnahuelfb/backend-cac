import psycopg2
from decouple import config

def get_connection():
  try:
    return psycopg2.connect(
      host=config('PGSQL_HOST'),
      user=config('PGSQL_USER'),
      password=config('PGSQL_PASSWORD'),
      database=config('PGSQL_DATABASE'),
    )
  except psycopg2.DatabaseError as ex:
    raise ex