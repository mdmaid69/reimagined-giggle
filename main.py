  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)