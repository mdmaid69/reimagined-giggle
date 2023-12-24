  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)