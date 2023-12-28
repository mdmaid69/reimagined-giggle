  import sqlite3
  def close_database_connection(connection):
        connection.close()
def remove_duplicates(lst):
        return list(set(lst))