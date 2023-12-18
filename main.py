import getpass
def get_username():
        return getpass.getuser()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)