  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_acceleration(speed, time):
        return speed / time