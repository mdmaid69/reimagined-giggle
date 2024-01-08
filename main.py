  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2