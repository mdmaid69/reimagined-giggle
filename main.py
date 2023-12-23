import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()