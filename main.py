  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)