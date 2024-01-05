  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()