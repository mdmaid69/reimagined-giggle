import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()