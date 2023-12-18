  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)