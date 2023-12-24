  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import collections
def create_priority_queue():
        return collections.deque()