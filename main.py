  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)