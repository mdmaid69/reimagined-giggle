  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import array
def get_array_buffer_info(array):
        return array.buffer_info()