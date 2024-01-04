import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)