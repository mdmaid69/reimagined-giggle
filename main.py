  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
  import sqlite3
  def close_database_connection(connection):
        connection.close()