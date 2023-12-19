import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import sqlite3
  def close_database_connection(connection):
        connection.close()