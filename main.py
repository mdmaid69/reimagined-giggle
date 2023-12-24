  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import sys
def add_to_python_path(path):
        sys.path.append(path)