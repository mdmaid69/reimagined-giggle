  import sqlite3
  def close_database_connection(connection):
        connection.close()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)