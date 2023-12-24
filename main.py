  import sqlite3
  def close_database_connection(connection):
        connection.close()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h