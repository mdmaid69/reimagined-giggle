import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)