  import sqlite3
  def close_database_connection(connection):
        connection.close()
  def convert_to_hex(n):
        return hex(n)