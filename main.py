import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()