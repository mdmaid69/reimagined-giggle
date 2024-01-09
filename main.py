  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import collections
def create_user_dict():
        return collections.UserDict()