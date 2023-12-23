  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_area(radius):
        return 3.14 * radius * radius