  import sqlite3
  def close_database_connection(connection):
        connection.close()
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)