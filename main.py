import array
def insert_into_array(array, i, item):
        array.insert(i, item)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()