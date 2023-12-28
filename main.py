import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import sqlite3
  def close_database_connection(connection):
        connection.close()