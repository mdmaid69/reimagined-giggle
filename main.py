  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_speed(distance, time):
        return distance / time