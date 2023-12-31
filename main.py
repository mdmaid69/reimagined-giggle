  import sqlite3
  def close_database_connection(connection):
        connection.close()
import collections
def create_user_dict():
        return collections.UserDict()