import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)