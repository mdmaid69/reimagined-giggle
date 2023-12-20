import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import sqlite3
  def close_database_connection(connection):
        connection.close()