import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()