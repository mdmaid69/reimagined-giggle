  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_work(force, distance):
        return force * distance