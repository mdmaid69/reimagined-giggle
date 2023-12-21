import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()