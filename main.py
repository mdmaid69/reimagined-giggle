  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)