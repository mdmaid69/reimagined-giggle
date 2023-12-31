  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}