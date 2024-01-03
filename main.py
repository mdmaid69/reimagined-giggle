  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)