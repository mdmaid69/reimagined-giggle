import random
def generate_random_number(start, end):
        return random.randint(start, end)
  import sqlite3
  def close_database_connection(connection):
        connection.close()