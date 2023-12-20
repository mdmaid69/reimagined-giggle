def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import sqlite3
  def close_database_connection(connection):
        connection.close()