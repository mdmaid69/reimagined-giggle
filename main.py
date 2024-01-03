  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_power(work, time):
        return work / time