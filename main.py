import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)