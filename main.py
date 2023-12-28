  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)