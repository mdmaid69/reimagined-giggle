import random
def generate_random_choice(choices):
        return random.choice(choices)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)