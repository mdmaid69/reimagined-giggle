import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)