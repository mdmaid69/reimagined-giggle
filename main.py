import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import sqlite3
  def close_database_connection(connection):
        connection.close()