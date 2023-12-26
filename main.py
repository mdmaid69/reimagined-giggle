  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)