  import sqlite3
  def close_database_connection(connection):
        connection.close()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"