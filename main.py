import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import sqlite3
  def close_database_connection(connection):
        connection.close()