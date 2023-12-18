  import sqlite3
  def close_database_connection(connection):
        connection.close()
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"