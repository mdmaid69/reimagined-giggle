import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()