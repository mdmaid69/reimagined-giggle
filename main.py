import array
def check_if_array_contains_item(array, item):
        return item in array
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()