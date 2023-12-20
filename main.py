  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_volume(length, width, height):
        return length * width * height