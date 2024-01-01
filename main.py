  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)