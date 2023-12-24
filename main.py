  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)