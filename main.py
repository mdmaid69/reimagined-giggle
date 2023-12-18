  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array