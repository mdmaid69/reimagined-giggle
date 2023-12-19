  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_pressure(force, area):
        return force / area