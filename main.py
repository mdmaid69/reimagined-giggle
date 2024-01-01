  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))