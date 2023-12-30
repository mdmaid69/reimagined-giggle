import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()