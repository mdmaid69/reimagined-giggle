  import sqlite3
  def close_database_connection(connection):
        connection.close()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)