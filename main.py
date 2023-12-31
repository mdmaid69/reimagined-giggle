  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h