import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()