  import sqlite3
  def close_database_connection(connection):
        connection.close()
def greet(name):
        print(f"Hello, {name}!")