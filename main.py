import collections
def create_stack():
        return collections.deque()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)