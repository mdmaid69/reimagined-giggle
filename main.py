  import sqlite3
  def close_database_connection(connection):
        connection.close()
import random
def roll_die():
        return random.randint(1, 6)