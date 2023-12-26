import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()