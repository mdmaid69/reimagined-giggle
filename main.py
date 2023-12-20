  import sqlite3
  def close_database_connection(connection):
        connection.close()
import random
def generate_random_choice(choices):
        return random.choice(choices)