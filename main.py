  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable