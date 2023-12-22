  import sqlite3
  def close_database_connection(connection):
        connection.close()
  def convert_to_binary(n):
        return bin(n)