import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)