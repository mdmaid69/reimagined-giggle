  import sqlite3
  def close_database_connection(connection):
        connection.close()
import glob
def find_files(pattern):
        return glob.glob(pattern)