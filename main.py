  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)