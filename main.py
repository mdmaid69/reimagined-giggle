  import sqlite3
  def close_database_connection(connection):
        connection.close()
def calculate_average(lst):
        return sum(lst) / len(lst)