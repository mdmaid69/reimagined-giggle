  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)