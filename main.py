import sys
def exit_program():
        sys.exit()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)