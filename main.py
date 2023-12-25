  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)