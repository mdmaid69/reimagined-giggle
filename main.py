  import sqlite3
  def close_database_connection(connection):
        connection.close()
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()