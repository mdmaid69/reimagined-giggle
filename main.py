import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
  import sqlite3
  def close_database_connection(connection):
        connection.close()