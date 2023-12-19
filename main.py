import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  import sqlite3
  def close_database_connection(connection):
        connection.close()