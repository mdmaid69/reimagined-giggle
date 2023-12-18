import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
  import sqlite3
  def close_database_connection(connection):
        connection.close()