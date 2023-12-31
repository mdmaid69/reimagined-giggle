  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_roi(gain, cost):
        return (gain - cost) / cost