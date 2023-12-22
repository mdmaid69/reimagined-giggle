import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
  import sqlite3
  def close_database_connection(connection):
        connection.close()