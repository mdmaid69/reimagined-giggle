import getpass
def get_username():
        return getpass.getuser()
  import sqlite3
  def close_database_connection(connection):
        connection.close()