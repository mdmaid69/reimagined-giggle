def is_palindrome(s):
        return s == s[::-1]
  import sqlite3
  def close_database_connection(connection):
        connection.close()