  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()