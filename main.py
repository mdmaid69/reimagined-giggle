  import sqlite3
  def close_database_connection(connection):
        connection.close()
def is_even(n):
        return n % 2 == 0