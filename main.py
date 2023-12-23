  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)