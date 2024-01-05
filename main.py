  import sqlite3
  def close_database_connection(connection):
        connection.close()
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"