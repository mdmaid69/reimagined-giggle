  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import glob
def find_files(pattern):
        return glob.glob(pattern)