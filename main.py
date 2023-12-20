  import sqlite3
  def close_database_connection(connection):
        connection.close()
import shutil
def delete_directory(path):
        shutil.rmtree(path)