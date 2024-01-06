import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()