  import sqlite3
  def close_database_connection(connection):
        connection.close()
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)