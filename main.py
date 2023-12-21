text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import sqlite3
  def close_database_connection(connection):
        connection.close()