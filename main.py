  import sqlite3
  def close_database_connection(connection):
        connection.close()
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)