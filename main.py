  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)