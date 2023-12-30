  import sqlite3
  def close_database_connection(connection):
        connection.close()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)