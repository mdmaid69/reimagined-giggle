import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()