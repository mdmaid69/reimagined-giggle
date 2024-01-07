import sys
print(sys.version)
  import sqlite3
  def close_database_connection(connection):
        connection.close()