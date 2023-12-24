  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_force(mass, acceleration):
        return mass * acceleration