  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list