import array
def pop_from_array(array, i=-1):
        return array.pop(i)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()