  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)