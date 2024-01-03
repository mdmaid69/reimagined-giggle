def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  import sqlite3
  def close_database_connection(connection):
        connection.close()