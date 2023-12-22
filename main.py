  import sqlite3
  def close_database_connection(connection):
        connection.close()
  def is_odd(n):
        return n % 2 != 0