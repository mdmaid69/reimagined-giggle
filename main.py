import platform
def get_python_version():
        return platform.python_version()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)