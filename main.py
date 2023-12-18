text = "Hello, world!"
print("Words:", len(text.split()))
  import sqlite3
  def close_database_connection(connection):
        connection.close()