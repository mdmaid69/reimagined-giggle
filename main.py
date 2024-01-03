import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)