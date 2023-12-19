  import sqlite3
  def close_database_connection(connection):
        connection.close()
text = "Hello, world!"
print("Reversed:", text[::-1])