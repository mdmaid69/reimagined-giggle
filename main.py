  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)