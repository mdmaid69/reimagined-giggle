  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)