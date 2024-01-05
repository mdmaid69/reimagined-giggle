  import sqlite3
  def close_database_connection(connection):
        connection.close()
  def calculate_area_circle(r):
        return 3.14 * r**2