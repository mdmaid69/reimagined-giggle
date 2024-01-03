  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))