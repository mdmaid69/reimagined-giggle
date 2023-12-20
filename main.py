import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()