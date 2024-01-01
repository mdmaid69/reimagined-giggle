  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"