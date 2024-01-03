import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import sqlite3
  def close_database_connection(connection):
        connection.close()