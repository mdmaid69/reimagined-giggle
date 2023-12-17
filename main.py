import collections
def create_counter():
        return collections.Counter()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)