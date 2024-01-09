  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_density(mass, volume):
        return mass / volume