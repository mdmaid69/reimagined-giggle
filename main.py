  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)