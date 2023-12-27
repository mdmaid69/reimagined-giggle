import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)