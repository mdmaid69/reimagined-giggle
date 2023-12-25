import array
def iterate_over_array(array):
        for item in array:
        print(item)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()