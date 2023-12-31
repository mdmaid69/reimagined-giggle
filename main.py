  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"