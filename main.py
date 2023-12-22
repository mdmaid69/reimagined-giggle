import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()